"""Drug Search Assistant.

This package groups the LangChain components taught in this module:

    config    -> settings (models, paths, RAG parameters)
    prompts   -> the agent's system prompt
    rag       -> load, split, embed, store, retrieve the drug reference,
                 and expose it as the `search_drugs` tool
    chain     -> the model and the `create_agent` agent
    assistant -> the end-to-end Drug Search Assistant workflow
"""
