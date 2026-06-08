import os
import shutil

import streamlit as st

from rag.pipeline import ask_question
from memory.chat_memory import clear_history
from ingestion.ingest import ingest_documents
from vision.image_analyzer import analyze_image


st.set_page_config(
    page_title="VisionAgent",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("🤖 VisionAgent")

if st.button("🗑️ Clear Chat"):

    clear_history()

    st.session_state[
        "question_input"
    ] = ""

    st.rerun()

st.write(
    "Upload documents or images and ask questions."
)

# ==========================================
# File Upload Section
# ==========================================

uploaded_files = st.file_uploader(
    "Upload Files",
    type=[
        "pdf",
        "txt",
        "docx",
        "jpg",
        "jpeg",
        "png"
    ],
    accept_multiple_files=True
)

if uploaded_files:

    # ==========================================
    # Image Preview
    # ==========================================

    image_files = [
        file for file in uploaded_files
        if file.name.lower().endswith(
            (
                ".jpg",
                ".jpeg",
                ".png"
            )
        )
    ]

    if image_files:

        if st.button(
            "🔍 Preview Image Analysis"
        ):

            os.makedirs(
                "temp_images",
                exist_ok=True
            )

            for image_file in image_files:

                image_path = os.path.join(
                    "temp_images",
                    image_file.name
                )

                with open(
                    image_path,
                    "wb"
                ) as f:

                    f.write(
                        image_file.getbuffer()
                    )

                with st.spinner(
                    f"Analyzing {image_file.name}..."
                ):

                    result = analyze_image(
                        image_path
                    )

                st.subheader(
                    f"🖼️ {image_file.name}"
                )

                st.write(result)

    # ==========================================
    # Process Documents
    # ==========================================

    if st.button(
        "📄 Process Documents"
    ):

        if os.path.exists(
            "data"
        ):

            shutil.rmtree(
                "data",
                ignore_errors=True
            )

        os.makedirs(
            "data",
            exist_ok=True
        )

        for uploaded_file in uploaded_files:

            file_path = os.path.join(
                "data",
                uploaded_file.name
            )

            with open(
                file_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

        with st.spinner(
            "Processing Files..."
        ):

            ingest_documents()

            clear_history()

            st.session_state[
                "question_input"
            ] = ""

        st.success(
            "Files Processed Successfully!"
        )

        st.rerun()

# ==========================================
# Question Answering
# ==========================================

question = st.text_input(
    "Ask a Question",
    key="question_input"
)

if question:

    with st.spinner(
        "Generating Answer..."
    ):

        try:

            result = ask_question(
                question
            )

            st.subheader(
                "Answer"
            )

            st.write(
                result["answer"]
            )

            st.subheader(
                "Sources"
            )

            for item in result[
                "sources"
            ]:

                filename = os.path.basename(
                    item["source"]
                )

                if item.get(
                    "page"
                ) is not None:

                    st.markdown(
                        f"📄 {filename} | Page {item['page'] + 1}"
                    )

                else:

                    st.markdown(
                        f"🖼️ {filename}"
                    )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )