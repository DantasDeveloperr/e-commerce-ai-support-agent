import json

from pathlib import Path

from src.embedding_client import create_embedding
from src.vector_search import cosine_similarity


EMBEDDINGS_PATH = Path("data/knowledge_embeddings.json")


def load_embeddings():
    with EMBEDDINGS_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def search_knowledge_semantic(query, top_k=3):
    query_vector = create_embedding(query)

    documents = load_embeddings()

    results = []

    for document in documents:

        similarity = cosine_similarity(
            query_vector,
            document["embedding"]
        )

        if similarity >= 0.65:
            results.append({
                "source": document["source"],
                "content": document["content"],
                "score": similarity
            })

    results.sort(
        key=lambda document: document["score"],
        reverse=True
    )

    return results[:top_k]