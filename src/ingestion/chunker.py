from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(
    docs,
    chunk_size=500,
    chunk_overlap=100
):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_documents(docs)

    return chunks
