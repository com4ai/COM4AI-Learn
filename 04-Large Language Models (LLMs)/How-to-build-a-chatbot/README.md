# How to Build a Chatbot

A chatbot is an application that exchanges messages with a user. Unlike a one-time LLM request, a chatbot keeps track of the conversation so that each new answer can use earlier messages as context.

```text
User message → chatbot application → language model → chatbot response
                         ↑                    ↓
                    conversation history ← saved message
```

For every turn, the application normally:

1. Receives a new user message.
2. Adds it to the conversation history.
3. Sends the relevant history to the model.
4. Saves and displays the model's response.

## Core Concepts

- **Conversation turn:** one user message and one chatbot response.
- **Messages:** a list of dictionaries with roles such as `system`, `user`, and `assistant`.
- **System instruction:** guidance that sets the chatbot's behavior, tone, or limits.
- **Conversation history:** prior messages supplied as context for the next response.
- **Chat interface:** the place where people send and read messages, such as a terminal, website, mobile app, Slack, or Teams.

## Types of Chatbots

| Type | How it works | Good for | Limitation |
|---|---|---|---|
| Rule-based | Follows predefined rules, menus, or decision trees. | Simple FAQs and fixed workflows. | Cannot handle unexpected language well. |
| Retrieval-based | Finds a response from a predefined set of answers or documents. | Support content and knowledge bases. | Does not naturally create new answers. |
| Generative LLM chatbot | An LLM generates a response token by token. | Natural conversation, writing help, and open questions. | Can hallucinate or give inaccurate answers. |
| Task-oriented chatbot | Guides users through a goal such as booking, ordering, or support. | Business processes with clear steps. | Requires reliable state and validation. |
| Hybrid chatbot | Combines LLM responses with rules, retrieval, APIs, or tools. | Production assistants that need both flexibility and control. | More components to design and maintain. |

## Ways to Build a Chatbot

### 1. Hosted LLM Chatbot

Use a provider's API and send the chat history with each turn.

```text
Terminal or web UI → Python application → LLM API → response
```

This is the fastest way to learn because the provider manages the model infrastructure. It requires an internet connection and usually has API costs.

### 2. Local Open-Weight Chatbot

Download an open-weight model and run it on your own computer.

```text
Terminal or web UI → Python application → local model → response
```

This can work offline after the model download and keeps messages on your own machine. Its quality and speed depend on the model and your hardware.

### 3. Rule-Based or Flow-Based Chatbot

Define intents, steps, forms, rules, and API calls explicitly.

```text
User message → intent or flow → business logic → predefined response
```

This approach is useful when correctness matters more than open-ended conversation, such as account support or a booking workflow.

### 4. Hybrid Chatbot

Combine an LLM with retrieved documents, business rules, APIs, and tools.

```text
User → chat application → LLM ↔ documents / APIs / rules → response
```

Most production assistants eventually become hybrid systems so they can answer naturally while still using trusted data and controlled actions.

## Architecture of a Simple LLM Chatbot

```text
┌──────────┐     ┌──────────────────────┐     ┌──────────────┐
│   User   │ ──▶ │ Chatbot Application  │ ──▶ │     LLM      │
└──────────┘     │ - message history    │     └──────────────┘
     ▲           │ - system instruction │            │
     └────────── │ - response display   │ ◀──────────┘
                 └──────────────────────┘
```

The chatbot application owns the history. The model does not automatically remember a previous terminal session unless the application sends those earlier messages again.

## Runnable Examples

All examples are terminal chatbots. Type `exit` to stop a conversation.

| File | Chatbot type | Requirements |
|---|---|---|
| `rule_based_chatbot.py` | Rule-based | Python only. |
| `local_chatbot.py` | Local open-weight | Python 3.12, `torch`, `transformers`, and the model download. |
| `hosted_chatbot.py` | Hosted LLM | `openai`, an `OPENAI_API_KEY`, internet access, and API credits. |
| `hybrid_chatbot.py` | Hybrid | The hosted requirements above; it answers selected FAQ topics from trusted local rules before asking the LLM. |

### 1. Rule-Based Chatbot

This chatbot matches words in the user's message to predefined answers. It does not call an LLM.

```python
RESPONSES = {
    "hello": "Hello! How can I help you?",
    "help": "You can say hello, ask about hours, or type exit.",
    "hours": "We are open Monday to Friday, 09:00 to 17:00.",
}

while True:
    message = input("You: ").strip().lower()
    if message == "exit":
        break

    answer = next(
        (reply for keyword, reply in RESPONSES.items() if keyword in message),
        "Bot: I only understand a few predefined questions.",
    )
    print(answer)
```

```bash
python rule_based_chatbot.py
```

### 2. Local Open-Weight Chatbot

This chatbot loads a model onto your computer and sends the conversation history to that local model. The `messages.append(...)` lines give the next response access to earlier turns.

```python
import torch
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-135M-Instruct",
    device=-1,
    torch_dtype=torch.float32,
)
messages = [{"role": "system", "content": "You are a helpful chatbot."}]

while True:
    user_message = input("You: ").strip()
    if user_message.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_message})
    response = generator(messages, max_new_tokens=100, do_sample=False)
    answer = response[0]["generated_text"][-1]["content"]
    messages.append({"role": "assistant", "content": answer})
    print(f"Bot: {answer}")
```

Use the local environment from the previous lesson, then run:

```bash
source ../How-to-talk-to-an-LLM/01-Getting-Started-with-an-LLM/.venv-open-weight/bin/activate
python local_chatbot.py
```

### 3. Hosted OpenAI Chatbot

This chatbot sends its conversation history to the OpenAI Responses API. You need an OpenAI Platform API key and API credits; a ChatGPT subscription alone does not provide them.

```python
import os
from openai import OpenAI

client = OpenAI()
messages = [{"role": "developer", "content": "You are a helpful chatbot."}]

while True:
    user_message = input("You: ").strip()
    if user_message.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_message})
    response = client.responses.create(model="gpt-5", input=messages)
    answer = response.output_text
    messages.append({"role": "assistant", "content": answer})
    print(f"Bot: {answer}")
```

Install the SDK and set your API key:

```bash
python -m pip install openai
export OPENAI_API_KEY="your_api_key_here"
python hosted_chatbot.py
```

ChatGPT subscriptions and OpenAI API billing are separate. This example needs API credits in the OpenAI Platform.

### 4. Hybrid Chatbot

The hybrid example uses rules for known support questions (`hours`, `refund`, and `email`) and uses the hosted LLM for other questions.

```python
TRUSTED_ANSWERS = {
    "hours": "Our support hours are Monday to Friday, 09:00 to 17:00.",
    "refund": "Refund requests can be submitted within 30 days of purchase.",
}

def find_trusted_answer(message):
    return next(
        (answer for keyword, answer in TRUSTED_ANSWERS.items()
         if keyword in message.lower()),
        None,
    )

# In the chatbot loop:
trusted_answer = find_trusted_answer(user_message)
if trusted_answer:
    answer = trusted_answer
else:
    response = client.responses.create(model="gpt-5", input=messages)
    answer = response.output_text
```

The complete version keeps conversation history and handles request errors in [hybrid_chatbot.py](hybrid_chatbot.py).

```bash
python hybrid_chatbot.py
```

Later, we will replace the small in-code FAQ with document retrieval, APIs, and tools.

## 📚 References

- [Previous lesson: How to Talk to an LLM](../How-to-talk-to-an-LLM/01-Getting-Started-with-an-LLM/README.md)
- [OpenAI: Developer quickstart](https://platform.openai.com/docs/quickstart/make-your-first-api-request)
- [Hugging Face: Chat templates](https://huggingface.co/docs/transformers/main/chat_templating_writing)
- [Rasa: Introduction to conversational AI assistants](https://rasa.com/docs/learn/introduction/)
