# Calvert Hall chatbot

This is the maintained repository for the Calvert Hall chatbot project. The Flask app answers questions about school material by searching a FAISS index for relevant passages and sending those passages and the question to an OpenAI model. It also lets users choose a suggested topic and ask a follow-up against the corresponding SQLite records.

- [Web routes](app.py) and [chat interface](templates/index.html)
- [Passage retrieval and answer generation](rag_chat.py)
- [Index builder](build_vector_store.py) and [database viewer](view_school_info.py)

The bundled database, search metadata and vector index belong together. The index contains 98 passages from the bundled database. Generating answers requires an OpenAI API key and makes hosted API calls.

Earlier versions are preserved in [CHCbot](https://github.com/Liamtechever/CHCbot) and [CHC_Chat_Bot](https://github.com/Liamtechever/CHC_Chat_Bot). Direct future changes and issues to this repository.
