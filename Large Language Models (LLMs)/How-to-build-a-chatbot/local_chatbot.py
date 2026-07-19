import torch
from transformers import pipeline


MODEL_NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"
SYSTEM_MESSAGE = "You are a helpful chatbot. Keep answers concise."


def main():
    print("Loading the local model. Type 'exit' to stop.")
    generator = pipeline(
        "text-generation",
        model=MODEL_NAME,
        device=-1,
        torch_dtype=torch.float32,
    )

    messages = [{"role": "system", "content": SYSTEM_MESSAGE}]

    while True:
        user_message = input("You: ").strip()

        if user_message.lower() == "exit":
            print("Bot: Goodbye!")
            break

        messages.append({"role": "user", "content": user_message})
        response = generator(messages, max_new_tokens=100, do_sample=False)
        answer = response[0]["generated_text"][-1]["content"]

        messages.append({"role": "assistant", "content": answer})
        print(f"Bot: {answer}")


if __name__ == "__main__":
    main()
