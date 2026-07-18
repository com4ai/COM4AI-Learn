import os

from openai import OpenAI


MODEL_NAME = "gpt-5"
SYSTEM_MESSAGE = "You are a helpful support chatbot. Keep answers concise."
TRUSTED_ANSWERS = {
    "hours": "Our support hours are Monday to Friday, 09:00 to 17:00.",
    "refund": "Refund requests can be submitted within 30 days of purchase.",
    "email": "You can contact support at support@example.com.",
}


def find_trusted_answer(message):
    message = message.lower()
    return next(
        (answer for keyword, answer in TRUSTED_ANSWERS.items() if keyword in message),
        None,
    )


def main():
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.")
        return

    client = OpenAI()
    messages = [{"role": "developer", "content": SYSTEM_MESSAGE}]

    print("Hybrid chatbot. Type 'exit' to stop.")

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        trusted_answer = find_trusted_answer(user_message)

        if trusted_answer:
            answer = trusted_answer
        else:
            request_messages = messages + [
                {"role": "user", "content": user_message}
            ]
            try:
                response = client.responses.create(
                    model=MODEL_NAME,
                    input=request_messages,
                )
            except Exception as error:
                print(f"Bot: Request failed: {error}")
                continue
            answer = response.output_text

        messages.extend(
            [
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": answer},
            ]
        )
        print(f"Bot: {answer}")


if __name__ == "__main__":
    main()
