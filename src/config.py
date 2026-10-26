"""Configuration only — no business logic lives here.

Everything that might change between environments (API key, model names,
RAG settings, file paths) is kept in one place so the rest of the code can
stay focused on LangChain concepts.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load variables from a local .env file (see .env.example).
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")



# --- Models ---------------------------------------------------------------
# gpt-4.1-mini with temperature 0 keeps drug reference answers consistent.
LLM_MODEL = "gpt-4.1-mini"
TEMPERATURE = 0

# text-embedding-3-small indexes the local drug reference.
EMBEDDING_MODEL = "text-embedding-3-small"

# --- RAG settings ---------------------------------------------------------
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150
RETRIEVER_K = 4

# --- Paths ----------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DRUG_REFERENCE_PATH = DATA_DIR / "DRUG_Handbook_2026.pdf"


def check_config() -> None:
    """Fail early with a clear message if the key or handbook is missing."""
    if not OPENAI_API_KEY:
        raise RuntimeError(
            "OPENAI_API_KEY is not set."
        )
    if not DRUG_REFERENCE_PATH.exists():
        raise FileNotFoundError(
            f"Drug reference not found at: {DRUG_REFERENCE_PATH}\n"
            "Place the drug reference PDF inside the data/ folder."
        )
