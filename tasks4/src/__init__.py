from openai import OpenAI

def main():
    client = OpenAI()

    # Two paragraph-length task descriptions
    task_descriptions = [
        """I need to create a new onboarding guide for new employees joining our company.
        The guide should include steps for setting up their email accounts, accessing the HR portal,
        completing compliance training, and scheduling an intro meeting with their team.""",

        """We are planning to redesign our company website to make it more user-friendly.
        The project involves working with the design team to improve the homepage layout,
        rewrite outdated content, test navigation, and ensure mobile responsiveness."""
    ]

    print("Summarizing tasks using ChatGPT-5-mini:\n")

    for idx, description in enumerate(task_descriptions, start=1):
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "You summarize tasks into short phrases."},
                {"role": "user", "content": description}
            ]
        )
        summary = response.choices[0].message.content.strip()
        print(f"Task {idx} summary: {summary}\n")

if __name__ == "__main__":
    main()

