from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

import ollama

from config import DB_DIR
from config import EMBEDDING_MODEL
from config import LLM_MODEL


embedding = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embedding
)


def ask(question):

    docs = db.similarity_search(question, k=3)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = f"""
You are an HR Assistant.

Answer ONLY using the provided context.

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"], docs