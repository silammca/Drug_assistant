"""LangChain v1 wiring: the model and the `create_agent` agent.

LangChain v1 note
-----------------

`bind_tools` only told the model which tools exist; we still had to run the
loop ourselves. `create_agent` builds the whole loop -- model call, tool call,
model call again. The LCEL RAG chain is gone because retrieval is now the
`search_drugs` tool.
"""

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from .config import LLM_MODEL, TEMPERATURE
from .prompts import DRUG_SYSTEM_PROMPT
from .tools import build_drug_search_tool


def build_llm() -> ChatOpenAI:
    return ChatOpenAI(model=LLM_MODEL, temperature=TEMPERATURE)


def build_agent(retriever):
    """Build the drug search agent: model + search tool + system prompt."""
    drug_search_tool = build_drug_search_tool(retriever)

    return create_agent(
        model=build_llm(),
        tools=[drug_search_tool],
        system_prompt=DRUG_SYSTEM_PROMPT,
    )
