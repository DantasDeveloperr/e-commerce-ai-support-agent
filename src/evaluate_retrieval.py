import pandas as pd

from semantic_search import search_knowledge_semantic


def evaluate_retrieval():
    dataset = pd.read_csv(
        "data/evaluation_dataset.csv",
        encoding="utf-8"
    )

    results = []

    for _, row in dataset.iterrows():
        question = row["question"]
        expected_source = row["expected_source"]

        retrieved_documents = search_knowledge_semantic(question)

        if retrieved_documents:
            actual_source = retrieved_documents[0]["source"]
        else:
            actual_source = "nenhum"

        success = actual_source == expected_source

        results.append({
            "question": question,
            "expected_source": expected_source,
            "actual_source": actual_source,
            "success": success
        })

        status = "ACERTO" if success else "ERRO"

        print(f"\nPergunta: {question}")
        print(f"Esperado: {expected_source}")
        print(f"Obtido:   {actual_source}")
        print(f"Resultado: {status}")

    results_df = pd.DataFrame(results)

    total = len(results_df)
    correct = results_df["success"].sum()
    accuracy = (correct / total) * 100 if total > 0 else 0

    print("\n" + "=" * 40)
    print("RESUMO DA AVALIAÇÃO")
    print("=" * 40)
    print(f"Total de perguntas: {total}")
    print(f"Acertos: {correct}")
    print(f"Erros: {total - correct}")
    print(f"Taxa de acerto: {accuracy:.2f}%")

    results_df.to_csv(
        "data/retrieval_evaluation_results.csv",
        index=False,
        encoding="utf-8"
    )

    print(
        "\nResultados salvos em "
        "data/retrieval_evaluation_results.csv"
    )


if __name__ == "__main__":
    evaluate_retrieval()