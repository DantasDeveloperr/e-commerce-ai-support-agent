import os
import time

from dotenv import load_dotenv
from google import genai
from google.genai import errors


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY não encontrada no arquivo .env")

client = genai.Client(
    api_key=api_key
)


def ask_llm(question):
    max_attempts = 3

    for attempt in range(max_attempts):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=question
            )

            return response.text

        except errors.ServerError as error:
            if attempt == max_attempts - 1:
                raise error

            wait_time = 2 ** attempt

            print(
                f"\nServiço temporariamente indisponível. "
                f"Nova tentativa em {wait_time} segundos..."
            )

            time.sleep(wait_time)