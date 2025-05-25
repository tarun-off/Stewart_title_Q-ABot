# Stewart_title_Q-ABot

# 🔍 Excel Semantic Search using ChromaDB + Groq + Streamlit

This project allows **natural language querying** over Excel datasets using **semantic search** powered by `ChromaDB` and **Groq's LLM** (like Mixtral or LLaMA3). It enables accurate, multi-row, context-aware search over structured Excel files using embeddings and vector similarity.

---

## 🚀 Features

- 📊 Upload and vectorize Excel data (row + column context)
- 💡 Ask natural language questions (e.g. *"Find all info about customer code ABFIR004"*)
- 🤖 Powered by Groq API (ultra-fast open-weight LLMs)
- 🧠 ChromaDB for high-speed vector retrieval
- 🧾 Streamlit frontend for interactive querying
- ✅ Pre-vectorized DB (no need to re-embed every time)
- 🔍 Multi-row retrieval, not just a single result

---

## 🏗️ Project Structure

```plaintext
.
├── app.py                  # Streamlit frontend (user chat + query engine)
├── chroma_utils.py                 # ChromaDB vector store directory
├── groq_utils.py                 # ChromaDB vector store directory
├── data/                   # Input Excel datasets
├── chroma_vector_db/ # Embedding, ingestion, formatting helpers
├── requirements.txt
└── README.md
