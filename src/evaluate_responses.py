import pandas as pd

from agent import process_message


def evaluate_responses():
    dataset = pd.read_csv(
        "data/evaluation_dataset.csv",
        encoding="utf-8"
    )

    results = []

    for _, row in dataset.iterrows():
        question = row["question"]
        expected_source = row["expected_source"]

        response = process_message(question)

        results.append({
            "question": question,
            "expected_source": expected_source,
            "response": response
        })

        print("\n" + "=" * 60)
        print(f"Pergunta: {question}")
        print(f"Fonte esperada: {expected_source}")
        print(f"Resposta do agente: {response}")

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        "data/response_evaluation_results.csv",
        index=False,
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print("AVALIAÇÃO CONCLUÍDA")
    print("=" * 60)
    print(f"Total de perguntas avaliadas: {len(results_df)}")
    print(
        "Resultados salvos em "
        "data/response_evaluation_results.csv"
    )


if __name__ == "__main__":
    evaluate_responses()