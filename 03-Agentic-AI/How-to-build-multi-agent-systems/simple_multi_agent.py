REFUND_POLICY = {
    "maximum_purchase_days": 30,
    "maximum_course_progress_percent": 20,
}


def policy_agent():
    """Return the approved refund policy for the coordinator."""
    print("Policy agent: Returning the refund policy.")
    return REFUND_POLICY


def eligibility_agent(request, policy):
    """Check user facts against the policy."""
    print("Eligibility agent: Checking purchase date and course progress.")
    within_refund_period = request["purchase_days_ago"] <= policy["maximum_purchase_days"]
    below_progress_limit = (
        request["course_progress_percent"] < policy["maximum_course_progress_percent"]
    )
    eligible = within_refund_period and below_progress_limit

    return {
        "eligible": eligible,
        "within_refund_period": within_refund_period,
        "below_progress_limit": below_progress_limit,
    }


def reviewer_agent(policy, eligibility):
    """Verify that the eligibility decision follows the policy."""
    print("Reviewer agent: Verifying the decision.")
    expected_eligibility = (
        eligibility["within_refund_period"] and eligibility["below_progress_limit"]
    )

    if eligibility["eligible"] != expected_eligibility:
        return {"approved": False, "reason": "The eligibility result is inconsistent."}

    if eligibility["eligible"]:
        return {
            "approved": True,
            "reason": (
                f"The purchase is within {policy['maximum_purchase_days']} days and "
                f"course progress is below {policy['maximum_course_progress_percent']}%."
            ),
        }

    return {
        "approved": True,
        "reason": "The request does not meet the refund policy requirements.",
    }


def coordinator_agent(request):
    """Coordinate the specialist agents and return a final result."""
    print("Coordinator agent: Delegating the refund request.")
    policy = policy_agent()
    eligibility = eligibility_agent(request, policy)
    review = reviewer_agent(policy, eligibility)

    if not review["approved"]:
        return {"eligible": None, "reason": review["reason"]}

    return {"eligible": eligibility["eligible"], "reason": review["reason"]}


def main():
    request = {
        "purchase_days_ago": 12,
        "course_progress_percent": 10,
    }

    print(f"Request: {request}")
    result = coordinator_agent(request)
    print(f"\nFinal decision: {result}")


if __name__ == "__main__":
    main()
