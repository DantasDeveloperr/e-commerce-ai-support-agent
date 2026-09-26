import pandas as pd


def evaluate_response_quality():
    dataset = pd.read_csv(
        "data/evaluation_dataset.csv",
        encoding="utf-8"
    )

    responses = pd.read_csv(
        "data/response_evaluation_results.csv",
        encoding="utf-8"
    )

    results = []

    for _, row in dataset.iterrows():
        question = row["question"]
        category = row["category"]
        expected_source = row["expected_source"]

        response_row = responses[
            responses["question"] == question
        ]

        if response_row.empty:
            continue

        response = response_row.iloc[0]["response"]

        has_response = bool(
            response and str(response).strip()
        )

        if category == "troca":
            expected_terms = [
                "7 dias",
                "número do pedido",
                "motivo",
                "sem sinais de uso"
            ]

        elif category in ["entrega", "atraso"]:
            expected_terms = [
                "pedido"
            ]

        elif category == "fora_do_escopo":
            expected_terms = [
                "não encontrei"
            ]

        else:
            expected_terms = []

        response_lower = str(response).lower()

        matched_terms = [
            term
            for term in expected_terms
            if term.lower() in response_lower
        ]

        if expected_terms:
            content_score = (
                len(matched_terms) / len(expected_terms)
            ) * 100
        else:
            content_score = 100

        if category == "fora_do_escopo":
            correct_out_of_scope_behavior = (
                "não encontrei informações suficientes"
                in response_lower
            )
        else:
            correct_out_of_scope_behavior = True

        results.append({
            "question": question,
            "category": category,
            "expected_source": expected_source,
            "has_response": has_response,
            "matched_terms": len(matched_terms),
            "expected_terms": len(expected_terms),
            "content_score": round(content_score, 2),
            "correct_out_of_scope_behavior":
                correct_out_of_scope_behavior
        })

    results_df = pd.DataFrame(results)

    results_df.to_csv(
        "data/response_quality_results.csv",
        index=False,
        encoding="utf-8"
    )

    print("\n" + "=" * 50)
    print("AVALIAÇÃO DA QUALIDADE DAS RESPOSTAS")
    print("=" * 50)

    print(
        f"Perguntas avaliadas: {len(results_df)}"
    )

    response_rate = (
        results_df["has_response"].mean() * 100
    )

    print(
        f"Taxa de respostas não vazias: "
        f"{response_rate:.2f}%"
    )

    average_content_score = (
        results_df["content_score"].mean()
    )

    print(
        f"Média de cobertura dos critérios: "
        f"{average_content_score:.2f}%"
    )

    out_of_scope = results_df[
        results_df["category"] == "fora_do_escopo"
    ]

    if not out_of_scope.empty:
        out_of_scope_accuracy = (
            out_of_scope[
                "correct_out_of_scope_behavior"
            ].mean() * 100
        )

        print(
            f"Comportamento correto fora do escopo: "
            f"{out_of_scope_accuracy:.2f}%"
        )

    print(
        "\nResultados salvos em "
        "data/response_quality_results.csv"
    )


if __name__ == "__main__":
    evaluate_response_quality()