import os

from openai import OpenAI


MODEL_NAME = "gpt-5"
SYSTEM_MESSAGE = "You are a helpful chatbot. Keep answers concise."


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.")
        return

    client = OpenAI()
    messages = [{"role": "developer", "content": SYSTEM_MESSAGE}]

    print("Hosted chatbot. Type 'exit' to stop.")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        messages.append({"role": "user", "content": user_message})

        try:
            response = client.responses.create(
                model=MODEL_NAME,
                input=messages,
            )
        except Exception as error:
            print(f"Bot: Request failed: {error}")
            messages.pop()
            continue

        answer = response.output_text
        messages.append({"role": "assistant", "content": answer})
        print(f"Bot: {answer}")


if __name__ == "__main__":
    main()
