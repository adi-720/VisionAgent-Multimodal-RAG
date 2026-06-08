from pathlib import Path

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

CHROMA_PATH = str(
    BASE_DIR / "chroma_db"
)

COLLECTION_NAME = "visionagent"


def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_vector_store(chunks):

    embeddings = get_embedding_model()

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME
    )


def load_vector_store():

    embeddings = get_embedding_model()

    return Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings,
        collection_name=COLLECTION_NAME
    )
