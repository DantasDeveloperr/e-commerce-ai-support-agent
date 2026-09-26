from semantic_search import search_knowledge_semantic


def test_search_exchange():
    results = search_knowledge_semantic(
        "Quero trocar um produto que comprei."
    )

    assert results
    assert results[0]["source"] == "trocas.txt"


def test_search_delivery():
    results = search_knowledge_semantic(
        "Qual é o prazo de entrega?"
    )

    assert results
    assert results[0]["source"] == "entrega.txt"


def test_search_out_of_scope():
    results = search_knowledge_semantic(
        "Como faço para declarar imposto de renda?"
    )

    assert results == []