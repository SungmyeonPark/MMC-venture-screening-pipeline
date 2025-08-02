# Rag-and-Langchain

This module implements a **Retrieval-Augmented Generation (RAG)** pipeline to score startup pitch decks using **LangChain**, **FAISS**, and **OpenAI GPT-4o**. It is designed to assist venture capital analysts in evaluating startups based on a configurable scorecard framework.

---

## Project Structure

Rag-and-Langchain/
├── app.py # FastAPI endpoint to serve pitch evaluation
├── embed_and_save.py # Extracts text from PDFs, embeds it, and builds FAISS index
├── evaluate_scorecard.py # Loads vector DB, retrieves relevant chunks, scores via LLM
├── scorecard_config.py # Configurable investment scorecard and prompt builder
├── GPT_LangChain_interactive.ipynb # (Notebook interface for development / testing)


---

## Installation

Make sure you have Python 3.8+ and the required packages:


PyMuPDF (for PDF parsing)

faiss-cpu or faiss-gpu (for vector search)

sentence-transformers

openai

langchain

uvicorn (to run FastAPI)

How It Works
Embed and Index

embed_and_save.py:

Loads pitch decks from a folder

Extracts and chunks text

Embeds using all-MiniLM-L6-v2

Stores embeddings in FAISS and metadata in a JSON file

Score a Company

evaluate_scorecard.py:

Matches company name to document chunks (via filename or embedding similarity)

Constructs prompts per category using a scorecard

Sends prompt to OpenAI’s gpt-4o

Parses and weights the scores to compute a total

Serve via API

app.py:

FastAPI POST endpoint /score

Accepts a company_name

Returns structured score breakdown

Run the Components
1. Embed PDFs (required before scoring)

python embed_and_save.py
This will create:

index.faiss

metadata.json

2. Launch the scoring API
   
uvicorn app:app --reload
Then send a POST request to:


POST http://localhost:8000/score
{
  "company_name": "AcmeAI"
}
3. Use the Notebook (optional)
Open GPT_LangChain_interactive.ipynb to experiment with retrieval and scoring logic in an interactive setting.

⚙️ Configuration
Scorecard
Edit scorecard_config.py to:

Adjust weights and criteria

Modify prompt templates

Environment
Set your OpenAI API key securely:

export OPENAI_API_KEY="sk-..."
Or store it in a .env file and load it using dotenv.


{
  "Strength of the Management Team": {
    "score": 3,
    "rationale": "Founders previously exited a successful startup.",
    "weighted_score": 0.3
  },
  ...
  "total_weighted_score": 0.85
}

Future Enhancements
Streamlit dashboard for visual analysis

MongoDB logging and feedback loop

CRM integration for deal pipeline tracking

License
MIT License
