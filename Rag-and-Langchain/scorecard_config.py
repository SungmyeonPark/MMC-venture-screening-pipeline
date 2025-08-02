# === Scorecard Criteria ===
scorecard_criteria = {
    "Strength of the Management Team": {
        "weight": 0.30, "max_score": 3,
        "subcriteria": [
            "Founders' experience and credibility",
            "Number of founders (preferably 2)",
            "Track record of previous ventures"
        ]
    },
    "Size of the Opportunity": {
        "weight": 0.25, "max_score": 3,
        "subcriteria": [
            "Market size",
            "Market segmentation",
            "Immediate addressable market"
        ]
    },
    "Product/Technology": {
        "weight": 0.15, "max_score": 3,
        "subcriteria": [
            "Innovation and uniqueness",
            "Technology viability",
            "Stage of development"
        ]
    },
    "Competitive Environment": {
        "weight": 0.10, "max_score": 3,
        "subcriteria": [
            "Market competition analysis",
            "Differentiation from competitors",
            "Competitive advantages"
        ]
    },
    "Marketing/Sales Channels/Partnerships": {
        "weight": 0.10, "max_score": 3,
        "subcriteria": [
            "Go-to-market strategy",
            "Existing partnerships",
            "Scalability of marketing"
        ]
    },
    "Need for Additional Investment": {
        "weight": 0.05, "max_score": 3,
        "subcriteria": [
            "Clear investment requirements",
            "Use of funds",
            "ROI projections"
        ]
    },
    "Other Factors": {
        "weight": 0.05, "max_score": 3,
        "subcriteria": [
            "Fit with investment thesis",
            "Cap table analysis",
            "Revenue model"
        ]
    }
}

# === Prompt Builder ===
def build_score_prompt(company, category, subcriteria, context):
    bullet = "\n".join(f"- {s}" for s in subcriteria)
    return f"""You are a VC analyst evaluating the pitch deck for {company}.

Category: {category}
Criteria:
{bullet}

Context:
\"\"\"
{context}
\"\"\"

Give a score from 0–3 based on the context.
Respond only in this JSON format:
{{
  "score": <integer>,
  "rationale": <short explanation based on evidence>
}}
"""