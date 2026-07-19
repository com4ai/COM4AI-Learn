# How to Build Multi-Agent AI Systems

A multi-agent AI system is an application where several agents work together on one goal. Each agent has a clear role, receives the information it needs, returns a result, and may pass that result to another agent.

For example, a customer-support system can delegate policy lookup to one agent, eligibility checking to another agent, and final verification to a reviewer agent.

```text
User request
     │
     ▼
Coordinator agent
     │
     ├── Policy agent       → finds the relevant policy
     ├── Eligibility agent  → checks the user's facts
     └── Reviewer agent     → verifies the conclusion
     │
     ▼
Final answer
```

## Why Use Multiple Agents?

Multiple agents let an application separate responsibilities. A specialist agent can have focused instructions, limited tools, and a clear output format.

This helps when a task needs different kinds of work, such as research, calculation, planning, verification, or an external action.

Examples of specialized roles:

| Agent role | Responsibility |
|---|---|
| Coordinator | Breaks a user goal into tasks and decides which agent receives each task. |
| Research agent | Finds relevant information from approved sources. |
| Data agent | Queries or processes structured data. |
| Planner agent | Creates an ordered plan for a multi-step task. |
| Action agent | Performs an allowed action using a tool or API. |
| Reviewer agent | Checks facts, completeness, safety, or formatting before the final response. |

Every agent should have a narrow responsibility. Creating many agents without a clear purpose adds cost and complexity.

## Core Components

| Component | Purpose |
|---|---|
| **Coordinator** | Receives the user goal, delegates work, and combines results. |
| **Specialist agents** | Perform focused tasks with their own instructions and tools. |
| **Messages** | Structured information exchanged between agents. |
| **Shared state** | The task details, results, and status that agents need to access. |
| **Tools** | Functions, APIs, search, databases, or other approved capabilities. |
| **Reviewer** | Validates results before a final action or answer. |
| **Guardrails** | Tool permissions, data-access rules, budgets, and step limits. |

## How Agents Coordinate

There are several common coordination patterns.

| Pattern | How it works | Example |
|---|---|---|
| **Supervisor** | One coordinator delegates tasks and receives all results. | A coordinator asks research and calculation agents for information. |
| **Sequential pipeline** | Each agent's output becomes the next agent's input. | Extract a document → summarize it → review the summary. |
| **Parallel specialists** | Independent agents work at the same time, then results are combined. | Research several sources at once. |
| **Reviewer pattern** | One agent creates a result and another checks it. | Draft a reply → check policy compliance → send for approval. |
| **Hierarchical** | A lead agent delegates to sub-coordinators, which delegate further. | Large projects with distinct workstreams. |

Start with a supervisor or sequential pipeline. They are easier to observe and debug than a large network of agents that can freely message each other.

## Messages and Shared State

Agents should exchange structured information instead of vague prose whenever possible.

```text
Task: Check refund eligibility

Input to eligibility agent:
{
  "purchase_days_ago": 12,
  "course_progress_percent": 10
}

Output from eligibility agent:
{
  "eligible": true,
  "reason": "Purchase is within 30 days and progress is below 20%."
}
```

Clear inputs and outputs make it easier to validate an agent's work, retry failed steps, and show why a final decision was made.

## A Simple Multi-Agent Architecture

```text
                         ┌─────────────────────┐
User request ──────────▶ │ Coordinator agent   │
                         │ - task state        │
                         │ - delegation rules  │
                         └──────────┬──────────┘
                                    │
              ┌─────────────────────┼─────────────────────┐
              ▼                     ▼                     ▼
      ┌──────────────┐      ┌──────────────┐      ┌──────────────┐
      │ Policy agent │      │ Eligibility  │      │ Reviewer     │
      │              │      │ agent        │      │ agent        │
      └──────┬───────┘      └──────┬───────┘      └──────┬───────┘
             │                     │                     │
             └───────────── results and checks ──────────┘
                                    │
                                    ▼
                              Final response
```

The application controls the flow. It decides which agents may run, what information they receive, which tools they can call, and when the system must stop.

## Guardrails and Safety

Multi-agent systems need clear limits because information and actions can move through several components.

- Give each agent only the tools and data it needs.
- Validate every message before passing it to another agent.
- Use a maximum number of agent calls and retries.
- Keep an audit log of delegation, tool calls, and outputs.
- Require user approval before sending messages, changing records, spending money, or deleting data.
- Do not allow one agent to give another agent broader permissions.
- Let a reviewer check important decisions, but do not treat a reviewer as a guarantee of correctness.

## Common Problems

| Problem | Likely cause | Improvement |
|---|---|---|
| Agents repeat the same work | Responsibilities overlap. | Give each agent a distinct role and clear stop condition. |
| Results conflict | Agents use different facts or assumptions. | Share validated state and define how the coordinator resolves conflicts. |
| The system is slow or expensive | Too many agent or tool calls. | Use fewer agents, parallelize only independent work, and set budgets. |
| An agent receives sensitive data | State is shared too broadly. | Minimize data passed to each agent and enforce access controls. |
| A final answer is unreliable | Results were not checked. | Add validation rules and a reviewer step for important tasks. |

## First Runnable Example

This example uses four small, safe roles:

1. **Coordinator agent:** delegates the refund request.
2. **Policy agent:** returns the refund rules.
3. **Eligibility agent:** checks the purchase date and course progress.
4. **Reviewer agent:** confirms that the decision follows the policy.

The complete code is in [simple_multi_agent.py](simple_multi_agent.py). It uses only Python's standard library.

Run it from this folder:

```bash
python3 simple_multi_agent.py
```

```python
def coordinator_agent(request):
    policy = policy_agent()
    eligibility = eligibility_agent(request, policy)
    review = reviewer_agent(policy, eligibility)

    return {
        "eligible": eligibility["eligible"],
        "reason": review["reason"],
    }
```

The coordination flow is:

```text
refund request → coordinator → policy + eligibility → reviewer → final decision
```

This first example does not call an LLM or an external service. It makes the message flow and responsibilities visible. In a later example, the same roles can use LLMs and approved tools.

## 📚 References

- [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155)
- [CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society](https://arxiv.org/abs/2303.17760)
