import pandas as pd


LOG_PATH = "data/conversation_logs.csv"


def load_logs():
    logs = pd.read_csv(
        LOG_PATH,
        encoding="utf-8"
    )

    return logs


if __name__ == "__main__":
    logs = load_logs()

    total_interactions = len(logs)

    interactions_with_context = logs["source"].notna().sum()

    interactions_without_context = logs["source"].isna().sum()

    retrieval_rate = (
        interactions_with_context / total_interactions
    ) * 100

    relevance = logs["relevance_score"].dropna()

    print("\n=== Métricas do agente ===\n")

    print(
        f"Total de interações: "
        f"{total_interactions}"
    )

    print(
        f"Interações com contexto: "
        f"{interactions_with_context}"
    )

    print(
        f"Interações sem contexto: "
        f"{interactions_without_context}"
    )

    print(
        f"Taxa de recuperação: "
        f"{retrieval_rate:.2f}%"
    )

    print(
        f"Similaridade média: "
        f"{relevance.mean():.4f}"
    )

    print(
        f"Similaridade mínima: "
        f"{relevance.min():.4f}"
    )

    print(
        f"Similaridade máxima: "
        f"{relevance.max():.4f}"
    )

    print("\n=== Documentos recuperados ===\n")

    print(
        logs["source"]
        .value_counts()
    )