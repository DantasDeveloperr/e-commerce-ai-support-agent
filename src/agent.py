import re

from gemini_client import ask_llm
from data_loader import find_order
from semantic_search import search_knowledge_semantic
from conversation_logger import log_conversation


conversation_state = {
    "waiting_for_order_id": False
}


def process_order(order_id):
    order = find_order(order_id)

    if order is None:
        return f"Não encontrei o pedido {order_id}."

    order_context = order.to_string()

    prompt = f"""
Você é um agente de atendimento de um e-commerce.

Dados encontrados no sistema para o pedido:

{order_context}

Responda ao cliente de forma clara, educada e objetiva.

Utilize somente as informações presentes nos dados do pedido.

Não invente informações que não estejam disponíveis.
"""

    return ask_llm(prompt)


def answer_from_knowledge(question):
    results = search_knowledge_semantic(question)

    if not results:
        return (
            "Não encontrei informações suficientes "
            "na minha base de conhecimento para responder.",
            None,
            None
        )

    relevant_document = results[0]

    context = relevant_document["content"]
    source = relevant_document["source"]
    score = relevant_document["score"]

    prompt = f"""
Você é um agente de atendimento de um e-commerce.

Utilize o contexto recuperado da base de conhecimento
para responder à pergunta do cliente.

CONTEXTO RECUPERADO:

Fonte: {source}

Relevância: {score:.4f}

{context}

PERGUNTA DO CLIENTE:

{question}

INSTRUÇÕES:

- Responda em português.
- Seja claro, educado e objetivo.
- Utilize somente as informações presentes no contexto.
- Não invente políticas, prazos ou procedimentos.
- Se o contexto não for suficiente para responder à pergunta,
  informe que não há informações suficientes.
"""

    response = ask_llm(prompt)

    return response, source, score


def process_message(message):
    response = None

    if conversation_state["waiting_for_order_id"]:
        match = re.search(r"\b\d{4}\b", message)

        if not match:
            response = "Por favor, informe um número de pedido válido."

            log_conversation(
                message,
                response
            )

            return response

        order_id = int(match.group())

        conversation_state["waiting_for_order_id"] = False

        response = process_order(order_id)

        log_conversation(
            message,
            response
        )

        return response

    match = re.search(r"\b\d{4}\b", message)

    if match:
        order_id = int(match.group())

        response = process_order(order_id)

        log_conversation(
            message,
            response
        )

        return response

    order_keywords = [
        "onde está meu pedido",
        "status do meu pedido",
        "status do pedido",
        "consultar meu pedido",
        "consultar pedido",
        "número do pedido"
    ]

    message_lower = message.lower()

    if any(keyword in message_lower for keyword in order_keywords):
        conversation_state["waiting_for_order_id"] = True

        response = (
            "Claro! Para consultar seu pedido, "
            "poderia me informar o número do pedido?"
        )

        log_conversation(
            message,
            response
        )

        return response

    response, source, relevance_score = answer_from_knowledge(message)

    log_conversation(
        message,
        response,
        source,
        relevance_score
    )

    return response