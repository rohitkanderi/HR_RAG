from langchain_chroma import Chroma
from config import DB_DIR


def create_vector_db(chunks, embedding):

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=DB_DIR
    )

    return db


def load_vector_db(embedding):

    return Chroma(
        persist_directory=DB_DIR,
        embedding_function=embedding
    )