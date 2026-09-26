from agent import process_message


def test_agent_exchange():
    response = process_message(
        "Quero trocar um produto que comprei."
    )

    assert response
    assert "7 dias" in response


def test_agent_delivery():
    response = process_message(
        "Qual é o prazo de entrega?"
    )

    assert response
    assert "região" in response.lower()


def test_agent_out_of_scope():
    response = process_message(
        "Como faço para declarar imposto de renda?"
    )

    assert response
    assert "não encontrei informações suficientes" in response.lower()