import pandas as pd


def analyze_evaluation():
    retrieval = pd.read_csv(
        "data/retrieval_evaluation_results.csv",
        encoding="utf-8"
    )

    quality = pd.read_csv(
        "data/response_quality_results.csv",
        encoding="utf-8"
    )

    print("\n" + "=" * 60)
    print("ANÁLISE CONSOLIDADA DA AVALIAÇÃO")
    print("=" * 60)

    # ----------------------------------------
    # RETRIEVAL
    # ----------------------------------------

    retrieval_accuracy = (
        retrieval["success"].mean() * 100
    )

    print("\n[RETRIEVAL]")
    print(
        f"Perguntas avaliadas: {len(retrieval)}"
    )
    print(
        f"Taxa de acerto: {retrieval_accuracy:.2f}%"
    )

    print("\nResultados por fonte:")

    retrieval_by_source = (
        retrieval
        .groupby("expected_source")["success"]
        .agg(["count", "sum"])
    )

    retrieval_by_source["accuracy"] = (
        retrieval_by_source["sum"]
        / retrieval_by_source["count"]
        * 100
    )

    print(retrieval_by_source)

    # ----------------------------------------
    # RESPONSE QUALITY
    # ----------------------------------------

    response_rate = (
        quality["has_response"].mean() * 100
    )

    average_content_score = (
        quality["content_score"].mean()
    )

    print("\n[QUALIDADE DAS RESPOSTAS]")
    print(
        f"Taxa de respostas não vazias: "
        f"{response_rate:.2f}%"
    )

    print(
        f"Média de cobertura dos critérios: "
        f"{average_content_score:.2f}%"
    )

    # ----------------------------------------
    # OUT OF SCOPE
    # ----------------------------------------

    out_of_scope = quality[
        quality["category"] == "fora_do_escopo"
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

    # ----------------------------------------
    # CATEGORIAS
    # ----------------------------------------

    print("\n[RESULTADOS POR CATEGORIA]")

    category_summary = (
        quality
        .groupby("category")
        .agg(
            questions=("question", "count"),
            average_content_score=(
                "content_score",
                "mean"
            )
        )
    )

    print(category_summary)

    # ----------------------------------------
    # FINAL
    # ----------------------------------------

    print("\n" + "=" * 60)
    print("ANÁLISE FINALIZADA")
    print("=" * 60)


if __name__ == "__main__":
    analyze_evaluation()