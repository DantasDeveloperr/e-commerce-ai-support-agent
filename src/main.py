from agent import process_message


while True:
    message = input("Cliente: ")

    if message.lower() == "sair":
        print("Atendimento encerrado.")
        break

    response = process_message(message)

    print("\nAgente:")
    print(response)
    print()