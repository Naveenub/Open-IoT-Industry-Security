from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from app.rag.vector_store import build_vector_store

vector_store = build_vector_store()

def get_ai_recommendation(query: str) -> str:
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        retriever=vector_store.as_retriever()
    )
    return qa.run(query)
