"""RAG over the drug reference: load, split, index, retrieve and search."""

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    EMBEDDING_MODEL,
    DRUG_REFERENCE_PATH,
    RETRIEVER_K,
)
from .tools import build_drug_search_tool


# STEP 1 — Load & Split
def load_and_split() -> list[Document]:
    loader = PyPDFLoader(str(DRUG_REFERENCE_PATH))
    documents = loader.load()
    if not any(document.page_content.strip() for document in documents):
        raise RuntimeError(
            f"The drug reference at {DRUG_REFERENCE_PATH} has no extractable text. "
            "Replace it with a searchable PDF or run OCR on it before starting the assistant."
        )
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    return splitter.split_documents(documents)


# STEP 2 — Store
def build_vector_store() -> InMemoryVectorStore:
    chunks = load_and_split()
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(chunks)
    return vector_store


# STEP 3 — Retrieve
def build_retriever():
    vector_store = build_vector_store()
    return vector_store.as_retriever(search_kwargs={"k": RETRIEVER_K})


