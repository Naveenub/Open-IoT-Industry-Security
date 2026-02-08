from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

def build_vector_store():
    docs = [
        Document(page_content="High CO levels indicate gas leakage."),
        Document(page_content="Smoke detection is an early fire signal."),
        Document(page_content="Temperature spikes may cause equipment failure.")
    ]

    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(docs, embeddings)
