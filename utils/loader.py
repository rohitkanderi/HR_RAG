from langchain_community.document_loaders import PyPDFDirectoryLoader


def load_documents(path):
    loader = PyPDFDirectoryLoader(path)
    return loader.load()