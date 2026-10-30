import tomllib
from google import genai
from google.genai import types

MODEL = "gemini-3.7-flash"

with open(".streamlit/secrets.toml", "rb") as f:
    key = tomllib.load(f)["GEMINI_API_KEY"]

client = genai.Client(api_key=key)

resp = client.models.generate_content(
    model=MODEL,
    contents="Hasil diagnosis: RAM bermasalah, keyakinan 80%. Jelaskan singkat.",
    config=types.GenerateContentConfig(
        system_instruction=(
            "Kamu teknisi servis laptop berpengalaman. Jelaskan dengan "
            "bahasa awam dan jawab hanya seputar laptop."
        )
    ),
)
print(resp.text)