import streamlit as st
from groq_utils import get_natural_language_response
from chroma_utils import query_top_match
import os
from pathlib import Path
import shutil

# Prevent tokenizer parallelism warning
os.environ["TOKENIZERS_PARALLELISM"] = "false"

st.set_page_config(page_title="Excel RAG Q&A", layout="centered")
st.title("🔍 Excel Q&A using ChromaDB + Groq")
st.markdown("Ask any question about your data and get a natural language answer powered by Groq!")

# Ensure 'data/' folder exists
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

#Files Upload
st.sidebar.header("📁 Upload Excel Files")
uploaded_files = st.sidebar.file_uploader(
    "Upload one or more Excel files (.xlsx)", type=["xlsx", "xls"], accept_multiple_files=True
)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = data_folder / uploaded_file.name
        with open(file_path, "wb") as f:
            shutil.copyfileobj(uploaded_file, f)
    st.sidebar.success(f"{len(uploaded_files)} file(s) saved to 'data/' folder ✅")

st.markdown("---")

# input
user_query = st.text_input("💬 Ask your question:", placeholder="e.g., What is the top-selling product in January?")

if st.button("Submit") and user_query:
    with st.spinner("🔎 Searching ChromaDB..."):
        matched_chunk = query_top_match(user_query)

    with st.spinner("🤖 Generating answer from Groq..."):
        prompt = f"""You are an AI assistant. Based on the following data, answer the question in clear natural language.

[Data]
{matched_chunk}

[Question]
{user_query}

[Answer]"""
        answer = get_natural_language_response(prompt)

    st.markdown("### 🧠 Answer:")
    st.success(answer)

    st.markdown("### 🗂️ Top Matching Data Snippet:")
    st.code(matched_chunk)
