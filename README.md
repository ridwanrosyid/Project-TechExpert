# Laptop Diagnostic Expert — Sistem Pakar Diagnosis Kerusakan Laptop

Prototype sistem pakar berbasis web yang mendiagnosis kerusakan laptop melalui konsultasi interaktif menggunakan **Backward Chaining** dan **Certainty Factor**.

## Fitur Utama

- **10 jenis kerusakan** laptop (K01-K10) terstruktur dalam Frame
- **25 gejala** (G01-G25) ditanyakan secara step-by-step
- **12 rule** inferensi (R1-R12) dengan Backward Chaining
- **Certainty Factor** untuk menghitung tingkat keyakinan diagnosis
- **Explanation Facility** — "Mengapa?" (Why) & "Bagaimana?" (How)
- **Visualisasi pohon inferensi** menggunakan Graphviz
- **Asisten AI (Gemini)** — menjelaskan hasil diagnosis dengan bahasa awam, dengan peran teknisi servis laptop

## Teknologi

| Komponen | Teknologi |
|---|---|
| UI Framework | Streamlit (Python) |
| Inference Engine | Python murni |
| Visualisasi | Graphviz |
| Asisten AI | Google Gemini (`google-genai`) |
| Testing | pytest + pytest-cov |

## Quick Start

### 1. Prasyarat

- Python 3.8 atau lebih baru
- Graphviz system binary ([download](https://graphviz.org/download/))

### 2. Instalasi

```bash
# Clone repositori project
git clone 

# Masuk ke direktori project
cd project-sistem-pakar

# Instal dependencies
pip install -r requirements.txt
```

**Pengaturan API Key (untuk fitur Asisten AI)**

Fitur "Penjelasan dari Asisten AI" membutuhkan API key Gemini milik masing-masing pengguna:

1. Buat API key di [Google AI Studio](https://aistudio.google.com/api-keys).
2. Buat file `.streamlit/secrets.toml` dengan isi satu baris:

```toml
GEMINI_API_KEY = "isi-api-key-kamu"
```

File `secrets.toml` berisi kunci pribadi, jadi **tidak disertakan** saat project dikumpulkan atau diunggah. Tanpa file ini aplikasi tetap berjalan, hanya fitur Asisten AI yang menampilkan pesan gagal dimuat.

### 3. Jalankan Aplikasi

```bash
streamlit run app.py

Buka browser di `http://localhost:8501`.
```

### 4. Jalankan Unit Test

```bash
# Semua test
pytest tests/ -v

# Dengan coverage report
pytest tests/ -v --cov=engine --cov=knowledge_base --cov-report=term-missing

# Test spesifik
pytest tests/test_certainty_factor.py -v
pytest tests/test_knowledge_base.py -v
pytest tests/test_backward_chaining.py -v
```

### 5. Linting

```bash
flake8 engine/ knowledge_base/ ui/ --max-line-length=120
```

## Struktur Folder

```
Project-Sistem-Pakar/
├── app.py                          # Entry point Streamlit
├── config.py                       # Konfigurasi & logging
├── requirements.txt                # Dependencies
├── pyproject.toml                  # Konfigurasi pytest
├── tes_ai.py                       # Skrip tes koneksi ke Gemini
├── README.md                       # Dokumen ini
│
├── knowledge_base/                 # Data Layer — Knowledge Base
│   ├── __init__.py                 # Fungsi akses publik
│   ├── frames.py                   # 10 Frame kerusakan (K01-K10)
│   ├── rules.py                    # 12 Rule IF-THEN (R1-R12)
│   └── symptoms.py                 # 25 Gejala (G01-G25)
│
├── engine/                         # Business Logic Layer
│   ├── __init__.py                 # Ekspor publik
│   ├── backward_chaining.py        # Mesin inferensi Backward Chaining
│   ├── certainty_factor.py         # Kalkulator CF
│   ├── explanation.py              # Explanation Facility (Why/How)
│   └── llm_explainer.py            # Penjelasan hasil diagnosis via Gemini
│
├── ui/                             # Presentation Layer
│   ├── __init__.py
│   ├── home.py                     # Halaman Beranda
│   ├── consultation.py             # Wizard Konsultasi
│   ├── result.py                   # Halaman Hasil Diagnosis
│   └── components.py               # Komponen UI reusable
│
├── visualization/                  # Visualisasi
│   ├── __init__.py
│   └── inference_tree.py           # Pohon inferensi (Graphviz)
│
├── tests/                          # Unit & Integration Tests
│   ├── __init__.py
│   ├── test_certainty_factor.py    # Test CF calculator
│   ├── test_knowledge_base.py      # Test integritas KB
│   └── test_backward_chaining.py   # Test BC engine
│
├── assets/                         # Static assets
│   └── style.css                   # Custom CSS
│
├── .streamlit/
│   ├── config.toml                 # Tema Streamlit (dark mode)
│   └── secrets.toml                # API key Gemini (pribadi, tidak dikumpulkan)
│
└── docs/                           # Dokumentasi teknis
    ├── project_charter.md          # Project Charter
    ├── srs_draft.md                # SRS (IEEE 830)
    ├── uml_analysis.md             # UML 2.5 Analysis
    ├── knowledge_base_design.md    # KB Design (ISO 9075)
    ├── architecture_design.md      # SDD (IEEE 1016)
    ├── sqap.md                     # SQAP (IEEE 730)
    ├── ui_design_spec.md           # UI Design (WCAG 2.1)
    └── api_spec.md                 # API Spec (OpenAPI 3.0)
```

## Konvensi Kode

| Aspek | Konvensi |
|---|---|
| Variabel & fungsi | `snake_case` |
| Class | `PascalCase` |
| Konstanta | `UPPER_SNAKE_CASE` |
| File/modul | `snake_case.py` |
| Standar | PEP 8 |
| Docstring | Google style |

## Dokumentasi

| Dokumen | Standar |
|---|---|
| [Project Charter](docs/project_charter.md) | — |
| [SRS](docs/srs_draft.md) | IEEE 830 |
| [UML Analysis](docs/uml_analysis.md) | UML 2.5 |
| [KB Design](docs/knowledge_base_design.md) | ISO/IEC 9075 |
| [Architecture](docs/architecture_design.md) | IEEE 1016 |
| [SQAP](docs/sqap.md) | IEEE 730 |
| [UI Design](docs/ui_design_spec.md) | WCAG 2.1 |
| [API Spec](docs/api_spec.md) | OpenAPI 3.0 |

---

## Tim Pengembang

Proyek ini dikembangkan oleh kelompok mahasiswa Ilmu Komputer UYM:

| Nama | NIM |
|---|---|
| Muhammad Ridwan Rosyid | 23050553 |
| Karina Nur Khaliza | 23050544 |

## tambahan yang Kami Lakukan

- Menambah fitur **Penjelasan dari Asisten AI** (`engine/llm_explainer.py` dan `ui/result.py`) yang menjelaskan hasil diagnosis memakai Google Gemini dengan peran teknisi servis laptop, termasuk percobaan ulang otomatis dan model cadangan saat server sibuk.
- Menambah skrip `tes_ai.py` untuk menguji koneksi ke Gemini.

---

> Laptop Diagnostic Expert — Projek Akhir Mata Kuliah Sistem Pakar, Oktober 2026