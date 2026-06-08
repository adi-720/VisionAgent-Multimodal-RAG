from pathlib import Path

from ingestion.loader import load_document
from ingestion.chunker import create_chunks

from vectordb.chroma_store import (
    create_vector_store,
    get_embedding_model,
    CHROMA_PATH,
    COLLECTION_NAME
)

from langchain_chroma import Chroma


BASE_DIR = (
    Path(__file__)
    .resolve()
    .parent
    .parent
    .parent
)

DATA_PATH = BASE_DIR / "data"


def ingest_documents(data_folder=DATA_PATH):

    try:

        db = Chroma(
            persist_directory=CHROMA_PATH,
            embedding_function=get_embedding_model(),
            collection_name=COLLECTION_NAME
        )

        db.delete_collection()

    except Exception:
        pass

    all_chunks = []

    files = list(
        Path(data_folder).iterdir()
    )

    for file_path in files:

        if file_path.is_file():

            docs = load_document(
                str(file_path)
            )

            chunks = create_chunks(
                docs
            )

            all_chunks.extend(
                chunks
            )

    create_vector_store(
        all_chunks
    )