import os
import openai
import faiss
import pickle
import numpy as np
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

INDEX_PATH = "vector_index.faiss"
META_PATH = "index_metadata.pkl"
EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4"
TOP_K = 3

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_query(query):
    response = client.embeddings.create(model=EMBED_MODEL, input=[query])
    return np.array(response.data[0].embedding).astype("float32")


def load_index_and_metadata():
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata

def generate_answer(question):
    index, metadata = load_index_and_metadata()
    query_vector = embed_query(question).reshape(1, -1)

    distances, indices = index.search(query_vector, 15)  # Search top 15 chunks

    def try_response(context_chunks):
        context = "\n\n".join(context_chunks)
        prompt = f"""You are a helpful assistant for Calvert Hall High School.
Here is relevant context from the school’s academic and policy database:

{context}

Now answer the following question as clearly and accurately as possible:
{question}
"""
        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()

    # Go through chunks in batches of 3
    for i in range(0, len(indices[0]), 3):
        chunk_batch = [metadata[i]["content"] for i in indices[0][i:i+3]]
        response = try_response(chunk_batch)

        if ("i don't know" not in response.lower()) and len(response) > 40:
            return response
        else:
            print(f"Batch {i//3 + 1} didn't work, trying next...")

    return "I'm sorry, I was unable to find this information in the database."




if __name__ == "__main__":
    while True:
        user_question = input("Ask: ")
        print(generate_answer(user_question))
