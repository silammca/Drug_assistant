"""Drug search tool exposed to the LangChain agent."""

from langchain_core.documents import Document
from langchain_core.tools import tool


def build_drug_search_tool(retriever):
    """Create the database search tool around the configured retriever."""

    @tool("search_drugs")
    def search_drugs(query: str) -> str:
        """Search the drug reference for medication information.

        Use for drug names, ingredients, uses, dosage forms, and other
        information available in the local drug reference. Do not use this
        tool to calculate doses or determine whether a medication is safe.

        query: The user's drug search in plain English.
        """
        documents: list[Document] = retriever.invoke(query)
        context = "\n\n".join(document.page_content for document in documents)
        return context or "No relevant information was found in the drug reference."

    return search_drugs
