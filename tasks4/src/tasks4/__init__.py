from __future__ import annotations

from openai import OpenAI

client = OpenAI(api_key="")


def summarize_task(paragraph: str) -> str:
    """
    Use Chat Completions with GPT-5-mini to turn a paragraph-length
    task description into a short phrase.
    """
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that summarizes tasks as a "
                    "very short phrase."
                ),
            },
            {
                "role": "user",
                "content": (
                    "Here is a task description:\n\n"
                    f"{paragraph}\n\n"
                    "Summarize this task as a short phrase."
                ),
            },
        ],
    )

    return response.choices[0].message.content.strip()


def main() -> None:
    """
    Simple loop: keep asking for task descriptions,
    summarize each one, stop on blank input.
    """
    print("=== Task Summarizer (GPT-5-mini) ===")
    print("Paste a paragraph-length task description.")
    print("Press Enter on an empty line to quit.\n")

    while True:
        paragraph = input("Task description (blank to quit):\n> ").strip()
        if not paragraph:
            print("Goodbye!")
            break

        try:
            short = summarize_task(paragraph)
            print(f"Summary: {short}\n")
        except Exception as e:
            print(f"[Error calling OpenAI API: {e}]\n")