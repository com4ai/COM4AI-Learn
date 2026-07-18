# How to Build an AI Agent

An AI agent is an application that works toward a goal by deciding what to do next, using tools when needed, observing the result, and repeating until it can provide a final answer.

For example, instead of only answering “What is the weather in Oslo?”, an agent could decide to call a weather tool, read the result, decide whether it needs more information, and then give the user a useful answer.

```text
User goal
   │
   ▼
Agent decides the next step
   │
   ├── Answer directly
   └── Use a tool
           │
           ▼
       Observe result
           │
           └── Decide again until finished
```

## The Agent Loop

The agent loop is the core pattern behind an AI agent.

```text
1. Receive a goal
2. Review available information and tools
3. Decide the next action
4. Run the action or tool
5. Observe the result
6. Repeat or return a final answer
```

```text
Goal: "Plan a meeting with the product team."
      │
      ├── Check the calendar
      ├── Find available times
      ├── Draft an invitation
      └── Ask for approval before sending it
```

The loop does not need to be complicated. A first agent can choose between only two or three safe tools. More capable agents may plan longer tasks, use many tools, and keep state across sessions.

## Core Components

| Component | Purpose |
|---|---|
| **Goal** | The task the user wants completed. It should be clear and bounded. |
| **LLM** | Interprets the goal and helps choose the next action. |
| **Tools** | Functions the agent can call, such as search, calculator, calendar, database, or API functions. |
| **Tool description** | Explains what each tool does, its inputs, and its limits so the LLM can choose it correctly. |
| **Observation** | The result returned by a tool. It becomes new information for the next decision. |
| **Memory or state** | Stores relevant conversation history, previous actions, and results. |
| **Agent loop** | Repeats decision, action, and observation until the task ends. |
| **Guardrails** | Limits the agent's tools, permissions, budgets, and number of steps. |

## Tools Give an Agent Capabilities

An LLM can produce text, but it cannot automatically access your files, calculate reliably, browse the web, send a message, or update a database. Tools provide those capabilities.

```text
LLM decision: "I need the total price."
                │
                ▼
         calculator tool
                │
                ▼
       observation: "Total = 84.50"
                │
                ▼
       LLM uses the result in its answer
```

Examples of agent tools:

| Tool | Example use |
|---|---|
| Calculator | Calculate a total, percentage, or conversion. |
| Knowledge-base search | Find information in approved documents. |
| Web search | Find current public information. |
| Database query | Look up an order, customer, or product. |
| Calendar | Check availability or draft a meeting. |
| Email or messaging | Draft or send a message after appropriate approval. |
| Code execution | Process data or run a controlled task. |

Every tool should have a narrow, clear purpose. Giving an agent unlimited access to the shell, database, or email is unsafe.

## Planning and Reasoning

Before using a tool, an agent may create a short plan. Planning is useful when a goal requires several dependent steps.

```text
Goal: "Tell me whether I can receive a refund."

Possible plan:
1. Search the refund policy with a knowledge-search tool.
2. Check the user's purchase date and course progress.
3. Compare those facts with the policy.
4. Explain the result and cite the policy.
```

## Memory and State

An agent needs some state to avoid repeating work and to use earlier results.

| Type | Example |
|---|---|
| **Short-term state** | The current user goal, tool calls, and observations during one task. |
| **Conversation history** | Earlier messages from the user and agent. |
| **Long-term memory** | Saved user preferences or durable facts, used carefully and with permission. |
| **External knowledge** | Documents returned by an approved search tool; this is not the same as memory. |

Keep only information relevant to the task. Too much history can make the agent slower, more expensive, and less reliable.

## A Simple Agent Architecture

```text
                        ┌──────────────────┐
User goal ────────────▶ │ Agent application │
                        │ - instructions   │
                        │ - state          │
                        │ - step limit     │
                        └────────┬─────────┘
                                 │
                                 ▼
                            LLM decision
                         ┌───────┴────────┐
                         │                │
                         ▼                ▼
                    final answer       tool call
                                           │
                                           ▼
                              calculator / search / API
                                           │
                                           ▼
                                     observation
                                           │
                                           └── back to LLM decision
```

The application, not the LLM, is responsible for running tools, saving state, enforcing permissions, and deciding when the loop must stop.

## Guardrails and Safety

Agents can take actions, so they need strong controls.

- **Allow only approved tools.** Do not let the model invent tool names or arbitrary commands.
- **Validate tool inputs.** Check types, ranges, required fields, and user permissions before performing an action.
- **Set a maximum step count.** Stop the loop after a small number of tool calls to prevent endless loops.
- **Limit data access.** A support agent should not access unrelated customer records.
- **Require approval for consequential actions.** Show the user a draft before sending an email, buying something, deleting data, or changing a record.
- **Log actions and observations.** Logs make it possible to debug and audit the agent.
- **Handle tool failures.** A failed API call should become an observation; the agent should not pretend it succeeded.

## Common Agent Problems

| Problem | Likely cause | Improvement |
|---|---|---|
| The agent loops forever | No step limit or no clear completion rule. | Set a maximum number of steps and a stop condition. |
| The agent chooses the wrong tool | Tool descriptions are vague or overlapping. | Use clear names, schemas, and examples. |
| The agent invents a tool result | The application did not verify the tool call. | Only accept observations returned by real tool code. |
| The agent takes an unsafe action | Permissions are too broad. | Use allow-lists and require human approval. |
| The agent gives a weak answer | It did not receive enough information. | Add better tools or a more specific workflow. |
| The task is expensive or slow | Too many model calls or tool calls. | Limit steps and use smaller, focused tools. |

## First Agent Example

This small example demonstrates the agent loop with two safe tools:

1. A calculator for simple arithmetic.
2. A knowledge-search tool that looks up information in a local support guide.

The `choose_action()` function plays the role of the agent's decision step. In a later example, an LLM will make that decision instead of simple rules.

The complete runnable code is in [simple_agent.py](simple_agent.py). It uses only Python's standard library, so no virtual environment or package installation is required.

Run it from this folder:

```bash
python3 simple_agent.py
```

```python
SUPPORT_GUIDE = {
    "hours": "Support is available Monday to Friday, 09:00 to 17:00 CET.",
    "refund": "Refund requests are accepted within 30 days of purchase.",
}


def calculator(expression):
    left, operator, right = expression.split()
    left, right = float(left), float(right)

    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        return left / right

    return "Unsupported operator."


def search_support_guide(query):
    query = query.lower()
    return next(
        (answer for keyword, answer in SUPPORT_GUIDE.items() if keyword in query),
        "No matching information was found.",
    )


def choose_action(goal):
    if any(operator in goal for operator in [" + ", " - ", " * ", " / "]):
        return "calculator", goal

    if "hours" in goal.lower() or "refund" in goal.lower():
        return "search_support_guide", goal

    return "answer", "I do not have an appropriate tool for this goal."


def run_agent(goal):
    print(f"Goal: {goal}")
    action, action_input = choose_action(goal)
    print(f"Agent decision: {action}")

    if action == "calculator":
        observation = calculator(action_input)
    elif action == "search_support_guide":
        observation = search_support_guide(action_input)
    else:
        observation = action_input

    print(f"Tool observation: {observation}")
    print(f"Final answer: {observation}")


run_agent("What are the support hours?")
run_agent("25 * 4")
```

Expected output:

```text
Goal: What are the support hours?
Agent decision: search_support_guide
Tool observation: Support is available Monday to Friday, 09:00 to 17:00 CET.
Final answer: Support is available Monday to Friday, 09:00 to 17:00 CET.

Goal: 25 * 4
Agent decision: calculator
Tool observation: 100.0
Final answer: 100.0
```

The example shows the essential agent pattern:

```text
goal → decision → tool → observation → final answer
```

It does not access the internet, modify files, or take external actions.

## 📚 References

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
