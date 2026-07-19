import torch
from transformers import pipeline


MODEL_NAME = "HuggingFaceTB/SmolLM2-135M-Instruct"


def main():
    print("Loading the model. The first run downloads it to your computer.")
    generator = pipeline(
        "text-generation",
        model=MODEL_NAME,
        device=-1,
        torch_dtype=torch.float32,
    )

    prompt = input("Ask the model a question: ")
    messages = [{"role": "user", "content": prompt}]

    response = generator(messages, max_new_tokens=100)
    answer = response[0]["generated_text"][-1]["content"]

    print("\nModel response:\n")
    print(answer)


if __name__ == "__main__":
    main()
