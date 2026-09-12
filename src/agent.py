import re

from gemini_client import ask_llm
from data_loader import find_order


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


def process_message(message):
    if conversation_state["waiting_for_order_id"]:
        match = re.search(r"\b\d{4}\b", message)

        if not match:
            return "Por favor, informe um número de pedido válido."

        order_id = int(match.group())

        conversation_state["waiting_for_order_id"] = False

        return process_order(order_id)

    match = re.search(r"\b\d{4}\b", message)

    if match:
        order_id = int(match.group())

        return process_order(order_id)

    conversation_state["waiting_for_order_id"] = True

    return "Claro! Para consultar seu pedido, poderia me informar o número do pedido?"