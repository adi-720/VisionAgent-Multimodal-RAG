from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader
)

from vision.image_to_document import (
    image_to_document
)


def load_document(file_path):

    extension = Path(file_path).suffix.lower()

    if extension == ".pdf":
        loader = PyPDFLoader(file_path)

    elif extension == ".txt":
        loader = TextLoader(file_path)

    elif extension == ".docx":
        loader = UnstructuredWordDocumentLoader(file_path)
    
    elif extension in [
        ".jpg",
        ".jpeg",
        ".png"
    ]:

        return image_to_document(
            file_path
        )
    else:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    return loader.load()