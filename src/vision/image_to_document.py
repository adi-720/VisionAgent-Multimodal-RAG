from langchain_core.documents import Document

from vision.image_analyzer import analyze_image


def image_to_document(image_path):

    description = analyze_image(
        image_path
    )

    doc = Document(
        page_content=description,
        metadata={
            "source": image_path,
            "type": "image"
        }
    )

    return [doc]