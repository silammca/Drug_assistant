# Drug Search Assistant

A command-line assistant that searches the local `DRUG_Handbook_2026.pdf` reference and uses the retrieved passages to answer medication information questions. It uses LangChain's agent loop with a single retrieval tool, `search_drugs`.

## What it does

- Loads and splits the local PDF when the application starts.
- Creates embeddings with OpenAI and stores the indexed chunks in memory for that run.
- Lets the model decide when to search the reference, then answers from the retrieved context.
- Runs in a terminal question-and-answer loop; enter `exit` or `quit` to stop.

The assistant does not include medication calculation, interaction checking, prescription validation, or allergy checking tools. It is not a substitute for advice from a qualified healthcare professional.

## Requirements

- Python 3.10 or newer
- An OpenAI API key with access to `gpt-4.1-mini` and `text-embedding-3-small`
- The reference PDF at `data/DRUG_Handbook_2026.pdf`

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # macOS / Linux
   source .venv/bin/activate
   # Windows PowerShell
   .venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your API key:

   ```dotenv
   OPENAI_API_KEY=your_key_here
   ```

4. Confirm the reference file exists at `data/DRUG_Handbook_2026.pdf`. The configured path is set in `src/config.py`.

## Run

From the project root, with the virtual environment active:

```bash
python app.py
```

The PDF is loaded and embedded at startup. This requires API access and can take a little time. The vector store is in memory, so the PDF is reprocessed on each launch. The app prints startup errors if the API key or reference PDF is missing.

## Example questions

- What is this medicine used for?
- What side effects does the handbook list for this medicine?
- Which medicines in the reference contain a particular ingredient?
- What medicines does the reference list for allergies?

Ask about information covered in the local handbook. The assistant may not find an answer if the PDF does not contain searchable text or relevant information.

## Project layout

```text
.
├── app.py                  # Terminal interface
├── requirements.txt        # Python dependencies
├── data/
│   └── DRUG_Handbook_2026.pdf
└── src/
    ├── assistant.py        # Builds the assistant and handles questions
    ├── chain.py            # Model and LangChain agent setup
    ├── config.py           # API key, model, retrieval settings, and paths
    ├── prompts.py           # Agent instructions
    ├── rag.py               # PDF loading, chunking, embeddings, and retrieval
    └── tools.py             # The search_drugs retrieval tool
```
