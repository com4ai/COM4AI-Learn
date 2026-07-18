from pathlib import Path

import numpy as np
import torch
from sentence_transformers import SentenceTransformer
from transformers import pipeline


KNOWLEDGE_BASE_PATH = Path("knowledge_base.txt")
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
CHUNK_SIZE = 500
NUMBER_OF_RESULTS = 2


def split_into_chunks(text: str, chunk_size: int) -> list[str]:
    """Split text into readable chunks without cutting a paragraph when possible."""
    paragraphs = [paragraph.strip() for paragraph in text.split("\n\n") if paragraph.strip()]
    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:
        if current_chunk and len(current_chunk) + len(paragraph) + 2 > chunk_size:
            chunks.append(current_chunk)
            current_chunk = paragraph
        else:
            current_chunk = f"{current_chunk}\n\n{paragraph}".strip()

    if current_chunk:
        chunks.append(current_chunk)

    return chunks


def retrieve(question: str, chunks: list[str], chunk_embeddings: np.ndarray, embedding_model):
    """Return the chunks whose embeddings are most similar to the question."""
    question_embedding = embedding_model.encode(
        question,
        normalize_embeddings=True,
    )
    similarity_scores = chunk_embeddings @ question_embedding
    result_indexes = np.argsort(similarity_scores)[-NUMBER_OF_RESULTS:][::-1]

    return [(chunks[index], float(similarity_scores[index])) for index in result_indexes]


def answer_question(question: str, context: str, generator) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                "You answer questions using only the supplied context. "
                "If the answer is not in the context, say: "
                "I do not know based on the provided document."
            ),
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}",
        },
    ]
    response = generator(messages, max_new_tokens=150, do_sample=False)
    return response[0]["generated_text"][-1]["content"]


def main():
    if not KNOWLEDGE_BASE_PATH.exists():
        print(f"Error: {KNOWLEDGE_BASE_PATH} was not found.")
        return

    print("Loading the document and embedding model...")
    document = KNOWLEDGE_BASE_PATH.read_text(encoding="utf-8")
    chunks = split_into_chunks(document, CHUNK_SIZE)

    embedding_model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    chunk_embeddings = embedding_model.encode(chunks, normalize_embeddings=True)

    print("Loading the local LLM...")
    generator = pipeline(
        "text-generation",
        model=LLM_MODEL_NAME,
        device=-1,
        torch_dtype=torch.float32,
    )

    print("RAG is ready. Ask about the support guide, or type 'exit' to stop.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Goodbye!")
            break

        if not question:
            continue

        results = retrieve(question, chunks, chunk_embeddings, embedding_model)
        context = "\n\n---\n\n".join(chunk for chunk, _ in results)
        answer = answer_question(question, context, generator)

        print(f"\nAnswer: {answer}")
        print("\nRetrieved source chunks:")
        for number, (chunk, score) in enumerate(results, start=1):
            print(f"\n[{number}] Similarity: {score:.3f}\n{chunk}")


if __name__ == "__main__":
    main()
