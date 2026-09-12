from pathlib import Path


KNOWLEDGE_BASE_PATH = Path("knowledge_base")


def load_knowledge_base():
    documents = []

    for file_path in KNOWLEDGE_BASE_PATH.glob("*.txt"):
        content = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents

def search_knowledge(query):
    documents = load_knowledge_base()

    stopwords = {
        "o", "a", "os", "as",
        "um", "uma",
        "de", "da", "do",
        "para", "por",
        "em", "no", "na",
        "e", "ou",
        "qual", "que",
        "me", "seu", "sua"
    }

    important_words = {
        "troca": 2,
        "trocar": 2,
        "trocas": 2,
        "entrega": 2,
        "entregar": 2,
        "atrasado": 2,
        "atrasada": 2,
        "cancelamento": 2,
        "cancelar": 2,
        "pagamento": 2
    }

    query_words = [
        word.lower().strip("?!.,")
        for word in query.split()
        if word.lower().strip("?!.,") not in stopwords
    ]

    results = []

    for document in documents:
        content = document["content"].lower()

        score = 0

        for word in query_words:
            weight = important_words.get(word, 1)

            if word in content:
                score += weight

        if score > 0:
            results.append({
                "source": document["source"],
                "content": document["content"],
                "score": score
            })

    results.sort(
        key=lambda document: document["score"],
        reverse=True
    )

    return results