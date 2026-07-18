# How to Build a Chatbot

## ❓ Question

How do I turn an LLM application into a chatbot that can hold a conversation?

## 🎯 Goal

Understand what a chatbot is, choose an appropriate chatbot design, and prepare to build a simple text-based chatbot.

## What Is a Chatbot?

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

## What We Will Build First

Our first example will be a terminal chatbot that:

1. Accepts messages in a loop.
2. Keeps the user and assistant messages in a Python list.
3. Sends the history to a hosted or local model.
4. Exits when the user types `exit`.

Later, we will add persistent memory, documents, tools, and a web interface.

## 📚 References

- [Previous lesson: How to Talk to an LLM](../How-to-talk-to-an-LLM/01-Getting-Started-with-an-LLM/README.md)
- [Hugging Face: Chat templates](https://huggingface.co/docs/transformers/main/chat_templating_writing)
- [Rasa: Introduction to conversational AI assistants](https://rasa.com/docs/learn/introduction/)
