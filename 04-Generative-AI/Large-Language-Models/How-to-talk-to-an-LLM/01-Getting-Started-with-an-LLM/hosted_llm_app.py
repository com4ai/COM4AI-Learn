import os

from openai import OpenAI


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.")
        print('Run: export OPENAI_API_KEY="your_api_key_here"')
        return

    client = OpenAI()
    prompt = input("Ask the AI a question: ")

    try:
        response = client.responses.create(
            model="gpt-5",
            input=prompt,
        )
        print("\nAI response:\n")
        print(response.output_text)
    except Exception as error:
        print(f"\nRequest failed: {error}")


if __name__ == "__main__":
    main()
