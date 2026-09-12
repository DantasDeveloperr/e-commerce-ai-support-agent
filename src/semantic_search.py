from src.knowledge_loader import load_knowledge_base
from src.embedding_client import create_embedding
from src.vector_search import cosine_similarity


def search_knowledge_semantic(query):
    query_vector = create_embedding(query)

    documents = load_knowledge_base()

    results = []

    for document in documents:
        document_vector = create_embedding(document["content"])

        similarity = cosine_similarity(
            query_vector,
            document_vector
        )

        results.append({
            "source": document["source"],
            "content": document["content"],
            "score": similarity
        })

    results.sort(
        key=lambda document: document["score"],
        reverse=True
    )

    return results