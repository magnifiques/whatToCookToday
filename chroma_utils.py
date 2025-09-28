import chromadb
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_chroma_db():
    
    embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb = Chroma(
        persist_directory="./chroma-db-langchain",
        embedding_function=embedding_function
    )
    return vectordb

def get_retriever():
    # Returns a retriever object for querying the Chroma DB
    vectordb = get_chroma_db()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    return retriever
