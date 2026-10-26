""" Drug Assistant — simple terminal interface.

Run with:  python app.py
"""

from src.assistant import DrugAssistant

SAMPLE_QUESTIONS = [
    "What is the Drug policy?",
    "What is this medicine used for?",
    "What are the common side effects of this medicine?",
]


def main() -> None:
    print("=" * 55)
    print(" Drug Assistant")
    print("=" * 55)
    print("Ask a question about Drug")
    print("Type 'exit' to quit.\n")
    print("Examples:")
    for example in SAMPLE_QUESTIONS:
        print(f"  - {example}")
    print()

    # Building the assistant loads and indexes the handbook (RAG). This runs
    # once at startup and may take a few seconds.
    # show_steps=True prints what RAG and the tools are doing, so the three
    # cases are visible during a demo. Use HRAssistant() for clean output.
    try:
        assistant = DrugAssistant(show_steps=True)
    except Exception as error:
        print(f"Startup error: {error}")
        return

    while True:
        try:
            question = input("Ask your Medicine Related question:\n> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye.")
            break

        if question.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break
        if not question:
            continue

        try:
            answer = assistant.ask(question)
            print("\n" + answer + "\n")
        except Exception as error:
            print(f"\nSorry, something went wrong: {error}\n")


if __name__ == "__main__":
    main()
