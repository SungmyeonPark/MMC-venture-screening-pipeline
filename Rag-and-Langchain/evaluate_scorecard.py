# evaluate_scorecard.py

import json, os, re, faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from scorecard_config import scorecard_criteria, build_score_prompt

EMBED_MODEL = "all-MiniLM-L6-v2"
GPT_MODEL = "gpt-4o"
INDEX_FILE = "index.faiss"
METADATA_FILE = "metadata.json"

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)
model = SentenceTransformer(EMBED_MODEL)
index = faiss.read_index(INDEX_FILE)
with open(METADATA_FILE) as f:
    metadata = json.load(f)

def extract_json_block(text):
    match = re.search(r"```json\s*({.*?})\s*```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    match2 = re.search(r"{.*}", text, re.DOTALL)
    return match2.group(0).strip() if match2 else text.strip()

def get_context(company, top_k=3):
    matches = [v["content"] for v in metadata.values() if company.lower() in v["source"].lower()]
    if not matches:
        print(" No filename matches, using embedding search")
        embed = model.encode([company], convert_to_numpy=True)
        D, I = index.search(embed, top_k)
        matches = [metadata[str(i)]["content"] for i in I[0]]
    return "\n\n".join(matches[:top_k])

def evaluate(company_name: str) -> dict:
    context = get_context(company_name)
    results = {}
    total = 0.0
    for cat, data in scorecard_criteria.items():
        prompt = build_score_prompt(company_name, cat, data["subcriteria"], context)
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You are a VC analyst scoring pitch decks."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=700
        )
        raw_output = response.choices[0].message.content.strip()
        clean = extract_json_block(raw_output)
        try:
            parsed = json.loads(clean)
        except json.JSONDecodeError:
            parsed = {"score": 0, "rationale": "⚠️ Could not parse LLM output."}

        weight = (parsed["score"] / data["max_score"]) * data["weight"]
        total += weight
        results[cat] = {
            "score": parsed["score"],
            "rationale": parsed["rationale"],
            "weighted_score": round(weight, 3)
        }

    results["total_weighted_score"] = round(total, 3)
    return results
