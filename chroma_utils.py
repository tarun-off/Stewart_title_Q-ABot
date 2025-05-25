import os
import chromadb
from chromadb.config import Settings, DEFAULT_TENANT, DEFAULT_DATABASE
#excel_vector_db
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

CHROMA_PATH = os.path.join(os.getcwd(), "chroma_rag_db")

def init_chroma_client():
    """Initializes and returns a PersistentClient connected to local ChromaDB."""
    client = chromadb.PersistentClient(
        path=CHROMA_PATH,
        settings=Settings(),
        tenant=DEFAULT_TENANT,
        database=DEFAULT_DATABASE,
    )
    return client

def get_collection(collection_name="excel_chunks"):
    """Gets or creates a collection from ChromaDB."""
    client = init_chroma_client()
    collection = client.get_or_create_collection(name=collection_name)
    return collection

def query_top_match(query_text: str, top_k: int = 5):
    """Queries the ChromaDB collection for top-k similar documents."""
    collection = get_collection()
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )
    documents = results.get("documents", [[]])[0]
    return documents[0] if documents else "No match found."
