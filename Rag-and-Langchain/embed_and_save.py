# embed_and_save.py
import os, json, fitz, faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

FOLDER_PATH = "/Users/equilibrium/MMC/pitchdecks"
EMBED_MODEL = "all-MiniLM-L6-v2"
INDEX_FILE = "index.faiss"
METADATA_FILE = "metadata.json"

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def extract_and_chunk(folder_path):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks_with_source = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            text = extract_text_from_pdf(os.path.join(folder_path, filename))
            chunks = splitter.split_text(text)
            for chunk in chunks:
                chunks_with_source.append({"source": filename, "content": chunk})
    return chunks_with_source

def main():
    embedder = SentenceTransformer(EMBED_MODEL)
    chunks = extract_and_chunk(FOLDER_PATH)
    texts = [c["content"] for c in chunks]
    sources = [c["source"] for c in chunks]
    embeddings = embedder.encode(texts, convert_to_numpy=True)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, INDEX_FILE)

    metadata = {i: {"source": sources[i], "content": texts[i]} for i in range(len(texts))}
    with open(METADATA_FILE, "w") as f:
        json.dump(metadata, f)

    print(f" Saved {len(texts)} embeddings to FAISS and metadata.")

if __name__ == "__main__":
    main()
