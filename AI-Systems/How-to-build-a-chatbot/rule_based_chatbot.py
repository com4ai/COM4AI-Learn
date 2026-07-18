RESPONSES = {
    "hello": "Hello! How can I help you?",
    "help": "You can say hello, ask about hours, or type exit.",
    "hours": "We are open Monday to Friday, 09:00 to 17:00.",
}


def main():
    print("Rule-based chatbot. Type 'exit' to stop.")

    while True:
        message = input("You: ").strip().lower()

        if message == "exit":
            print("Bot: Goodbye!")
            break

        answer = next(
            (response for keyword, response in RESPONSES.items() if keyword in message),
            "Bot: I only understand a few predefined questions.",
        )
        print(answer)


if __name__ == "__main__":
    main()
