from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectordb import create_vector_db

from config import DOCS_DIR


def main():

    print("Loading PDFs...")

    docs = load_documents(DOCS_DIR)

    print(f"{len(docs)} pages loaded")

    chunks = split_documents(docs)

    print(f"{len(chunks)} chunks created")

    embedding = get_embeddings()

    create_vector_db(chunks, embedding)

    print("Vector database created successfully")


if __name__ == "__main__":
    main()