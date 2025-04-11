import sqlite3

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import json
import re
from rag_chat import generate_answer, load_index_and_metadata, embed_query, TOP_K, CHAT_MODEL, client

# Importing your RAG pipeline

load_dotenv()

app = Flask(__name__)

# Load labeled resource links (optional, if you're still using them elsewhere)
with open("calvert_hall_urls_clean_labeled.json", encoding="utf-8") as f:
    resource_links = json.load(f)

# Load feedback database
FEEDBACK_DB_PATH = "feedback_db.json"
if os.path.exists(FEEDBACK_DB_PATH):
    with open(FEEDBACK_DB_PATH, encoding="utf-8") as f:
        feedback_db = json.load(f)
else:
    feedback_db = {}

def save_feedback():
    with open(FEEDBACK_DB_PATH, "w", encoding="utf-8") as f:
        json.dump(feedback_db, f, indent=2, ensure_ascii=False)

def get_all_topics():
    conn = sqlite3.connect("school_info.db")
    c = conn.cursor()
    c.execute("SELECT DISTINCT topic FROM info")
    rows = c.fetchall()
    conn.close()
    return [row[0] for row in rows]



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['message'].strip()

    try:
        # Generate RAG response with access to FAISS indices and metadata
        index, metadata = load_index_and_metadata()
        query_vector = embed_query(user_message).reshape(1, -1)
        distances, indices = index.search(query_vector, TOP_K + 3)

        # Get fallback topics (max 3 unique topics)
        seen = set()
        top_topics = []
        for i in indices[0]:
            topic = metadata[i]["topic"]
            if topic not in seen:
                seen.add(topic)
                top_topics.append(topic)
            if len(top_topics) == 3:
                break

        # Try generating a response
        answer = generate_answer(user_message)
        print("Generated Answer:", answer)

        # Fallback logic
        fallback_phrases = [
            "i don't know",
            "i do not know",
            "the text does not provide",
            "no relevant information",
            "i’m sorry, i was unable to find",
            "does not provide specific information on"
        ]

        needs_user_choice = any(
            phrase in answer.lower() for phrase in fallback_phrases
        ) or len(answer) < 40

        return jsonify({
            'message': answer,
            'fallback_topics': top_topics,
            'needs_user_choice': needs_user_choice
        })

    except Exception as e:
        print("RAG Error:", e)

    return jsonify({'message': "Something went wrong. Try again later."})


@app.route('/feedback', methods=['POST'])
def feedback():
    question = request.form['question'].strip()
    corrected = request.form['corrected'].strip()
    if question and corrected:
        feedback_db[question] = corrected
        save_feedback()
        return jsonify({'status': 'saved'})
    return jsonify({'status': 'error', 'message': 'Missing data'})

@app.route('/ask_topic', methods=['POST'])
def ask_topic():
    topic = request.form['topic'].strip()
    question = request.form['question'].strip()

    conn = sqlite3.connect("school_info.db")
    c = conn.cursor()
    c.execute("SELECT content FROM info WHERE topic = ?", (topic,))
    rows = c.fetchall()
    conn.close()

    if rows:
        combined_context = "\n\n".join([row[0] for row in rows])
        prompt = f"""You are a helpful assistant for Calvert Hall High School.
Here is context from the topic **{topic}**:

{combined_context}

Now answer this question: {question}
"""
        response = client.chat.completions.create(
            model=CHAT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return jsonify({'message': response.choices[0].message.content.strip()})

    return jsonify({'message': "That topic did not return any content."})


if __name__ == '__main__':
    app.run(debug=True)
