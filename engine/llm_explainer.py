import time

import streamlit as st
from google import genai
from google.genai import types

# Daftar model yang dicoba berurutan. Kalau model pertama sibuk/tidak
# tersedia, otomatis coba model berikutnya.
MODELS = ["gemini-3.7-flash", "gemini-2.5-flash"]

# Berapa kali mencoba ulang tiap model kalau server sedang sibuk (503)
MAX_PERCOBAAN = 3
JEDA_DETIK = 2

SYSTEM_PROMPT = (
    "Kamu adalah teknisi servis laptop berpengalaman. "
    "Kamu menerima hasil diagnosis dari sistem pakar (nama kerusakan "
    "dan tingkat keyakinan). Jelaskan dengan bahasa awam apa artinya, "
    "kemungkinan penyebabnya, dan langkah perbaikan awal. "
    "Jangan mengubah hasil diagnosis dari sistem pakar. "
    "Jawab hanya seputar laptop. Jawab singkat dan jelas."
)


def jelaskan_diagnosis(nama_kerusakan, cf_final, pertanyaan=None):
    """Minta Gemini menjelaskan hasil diagnosis. Mengembalikan teks."""
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    except Exception as e:
        return f"Maaf, penjelasan AI tidak bisa dimuat. Cek API key. ({e})"

    isi = (
        f"Hasil sistem pakar: {nama_kerusakan} "
        f"dengan tingkat keyakinan {cf_final * 100:.1f}%."
    )
    if pertanyaan:
        isi += f"\nPertanyaan pengguna: {pertanyaan}"

    config = types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT)
    error_terakhir = None

    for model in MODELS:
        for percobaan in range(1, MAX_PERCOBAAN + 1):
            try:
                resp = client.models.generate_content(
                    model=model, contents=isi, config=config
                )
                return resp.text
            except Exception as e:
                error_terakhir = e
                pesan = str(e)
                # 503 = server sibuk, 429 = kuota/terlalu sering: coba lagi
                if "503" in pesan or "429" in pesan:
                    time.sleep(JEDA_DETIK * percobaan)
                    continue
                # Error lain (misal model tidak ada): ganti ke model berikutnya
                break

    return (
        "Maaf, server AI sedang sibuk. Silakan coba lagi sebentar lagi. "
        f"({error_terakhir})"
    )