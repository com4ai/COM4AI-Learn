SUPPORT_GUIDE = {
    "hours": "Support is available Monday to Friday, 09:00 to 17:00 CET.",
    "refund": "Refund requests are accepted within 30 days of purchase.",
}


def calculator(expression):
    """Calculate an expression written as: number operator number."""
    left, operator, right = expression.split()
    left, right = float(left), float(right)

    if operator == "+":
        return left + right
    if operator == "-":
        return left - right
    if operator == "*":
        return left * right
    if operator == "/":
        if right == 0:
            return "Cannot divide by zero."
        return left / right

    return "Unsupported operator."


def search_support_guide(query):
    """Search a small approved knowledge base."""
    query = query.lower()
    return next(
        (answer for keyword, answer in SUPPORT_GUIDE.items() if keyword in query),
        "No matching information was found.",
    )


def choose_action(goal):
    """Choose the next agent action from the user's goal."""
    if any(operator in goal for operator in [" + ", " - ", " * ", " / "]):
        return "calculator", goal

    if "hours" in goal.lower() or "refund" in goal.lower():
        return "search_support_guide", goal

    return "answer", "I do not have an appropriate tool for this goal."


def run_agent(goal):
    """Run one safe decision-action-observation loop."""
    print(f"\nGoal: {goal}")
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


def main():
    run_agent("What are the support hours?")
    run_agent("25 * 4")


if __name__ == "__main__":
    main()
