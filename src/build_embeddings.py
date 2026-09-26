import json
from pathlib import Path

from knowledge_loader import load_knowledge_base
from embedding_client import create_embedding


OUTPUT_PATH = Path("data/knowledge_embeddings.json")


def build_embeddings():
    documents = load_knowledge_base()

    embeddings = []

    for document in documents:
        print(f"Gerando embedding: {document['source']}")

        vector = create_embedding(document["content"])

        embeddings.append({
            "source": document["source"],
            "content": document["content"],
            "embedding": vector
        })

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(embeddings, file)

    print("\nEmbeddings salvos com sucesso.")


if __name__ == "__main__":
    build_embeddings()