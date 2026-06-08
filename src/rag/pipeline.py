from vectordb.chroma_store import load_vector_store
from llm.groq_client import get_llm_client


def ask_question(question):

    db = load_vector_store()

    results = db.similarity_search(
        question,
        k=3
    )

    if not results:

        return {
            "answer":
            "No relevant information found.",
            "sources": []
        }

    sources = []

    for doc in results:

        source = doc.metadata.get(
            "source",
            "Unknown"
        )

        page = doc.metadata.get(
            "page"
        )

        sources.append(
            {
                "source": source,
                "page": page
            }
        )

    # Remove duplicate sources
    unique_sources = []

    seen = set()

    for item in sources:

        key = (
            item["source"],
            item["page"]
        )

        if key not in seen:

            seen.add(key)

            unique_sources.append(
                item
            )

    context = "\n\n".join(
        [
            doc.page_content
            for doc in results
        ]
    )

    prompt = f"""
Answer ONLY from the provided context.

Context:
{context}

Question:
{question}

Rules:
1. Use ONLY the context.
2. Do NOT use outside knowledge.
3. If the answer is not present in the context, reply:
"I could not find this information in the uploaded documents."
"""

    client = get_llm_client()

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = (
        response
        .choices[0]
        .message
        .content
    )

    return {
        "answer": answer,
        "sources": unique_sources
    }
