import csv
from datetime import datetime
from pathlib import Path


LOG_PATH = Path("data/conversation_logs.csv")


def log_conversation(
    user_message,
    assistant_response,
    source=None,
    relevance_score=None
):
    file_exists = LOG_PATH.exists() and LOG_PATH.stat().st_size > 0

    with LOG_PATH.open(
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "user_message",
                "assistant_response",
                "source",
                "relevance_score"
            ])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow([
            timestamp,
            user_message,
            assistant_response,
            source,
            relevance_score
        ])