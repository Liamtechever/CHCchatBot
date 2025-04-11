import sqlite3

import numpy as np
import openai
import os
import faiss
import pickle
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


DB_PATH = "school_info.db"
INDEX_PATH = "vector_index.faiss"
META_PATH = "index_metadata.pkl"

EMBED_MODEL = "text-embedding-3-small"
CHUNK_SIZE = 1000

def chunk_text(text, chunk_size=CHUNK_SIZE):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def get_all_chunks():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT topic, content FROM info")
    rows = c.fetchall()
    conn.close()

    chunks = []
    metadata = []
    for topic, content in rows:
        split_chunks = chunk_text(content)
        for chunk in split_chunks:
            chunks.append(chunk)
            metadata.append({"topic": topic, "content": chunk})
    return chunks, metadata

def embed_texts(texts):
    embeddings = []
    for i in range(0, len(texts), 100):
        batch = texts[i:i+100]
        response = client.embeddings.create(model=EMBED_MODEL, input=batch)
        embeddings.extend([e.embedding for e in response.data])
    return embeddings


if __name__ == "__main__":
    print("Loading and chunking data...")
    chunks, metadata = get_all_chunks()

    print(f"Generating embeddings for {len(chunks)} chunks...")
    vectors = embed_texts(chunks)

    print("Saving FAISS index and metadata...")
    dimension = len(vectors[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors).astype("float32"))

    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)

    print("Done! Vector index built.")
