# Drug Search Assistant

## Business Problem

Users need a simple way to search a local drug reference for medication
information. This assistant retrieves relevant passages from the supplied PDF
and answers using that source.

## Objective

Build a working drug search assistant using LangChain components, with
retrieval exposed to the agent as the `search_drugs` tool.

## LangChain Concepts

- System Prompt
- RAG
- Retriever (exposed as a tool)
- LLM
- Tool Calling
- Tool Validation
- Agent (`create_agent`)

## Architecture

The agent decides first whether a tool is needed. RAG is **not** a mandatory
first step — it runs only for knowledge questions, as the `search_drugs`
tool.

## Project Structure

```
hr_assistant/
├── app.py                 # Terminal interface — ask questions in a loop.
├── .env.example           # Template for your OpenAI API key.
├── requirements.txt       # Python dependencies.
├── README.md              # This file.
├── data/
│   └── DRUG_Handbook_2026.pdf   # Drug reference RAG source.
├── src/
    ├── config.py          # Settings: model names, RAG params, file paths.
    ├── prompts.py         # The agent's system prompt.
    ├── rag.py             # Load, split, embed, retrieve + the search_drugs tool.
    ├── chain.py           # The model and the create_agent agent.
    └── assistant.py       # Builds the agent and answers a question.

```

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```

2. Install the requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. Create your `.env` file from the template and add your key:

   ```bash
   # .env
   OPENAI_API_KEY=your_key_here
   ```

## Run

```bash
python app.py
```

The drug reference is loaded and indexed once at startup, then you can ask questions
in a loop.

## Example Questions

- What is this medicine used for?
- What are the common side effects listed for this medicine?
- What ingredients are listed for this medicine?
- Search the reference for medicines used for allergies.
