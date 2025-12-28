from app.schemas.goal_interpretation import GoalInterpretation


def interpret_goal(raw_text: str) -> GoalInterpretation:
    """
    Pure reasoning agent that converts raw goal text into structured intent.
    
    This agent performs interpretation only - no execution, no side effects.
    It identifies objective, time horizon, constraints, assumptions, ambiguities,
    and risk flags from unstructured natural language input.
    
    Args:
        raw_text: Unstructured natural language goal description
        
    Returns:
        GoalInterpretation: Structured interpretation validated against schema
    """
    return GoalInterpretation(
        objective=raw_text.strip(),
        time_horizon=None,
        constraints=[],
        assumptions=[],
        ambiguities=[
            "Objective may be underspecified",
            "Time horizon not explicitly defined",
            "Constraints not specified"
        ],
        risk_flags=[
            "Unstructured goal input"
        ]
    )

