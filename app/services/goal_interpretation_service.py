from sqlalchemy.orm import Session

from app.db.models import Goal, GoalInterpretation
from app.agents.goal_interpreter import interpret_goal


def persist_goal_interpretation(goal: Goal, raw_text: str, db: Session) -> GoalInterpretation:
    """
    Persists a goal interpretation by calling the interpreter agent and storing the result.
    
    The agent is called to interpret the raw text, and the structured interpretation
    is persisted as an immutable record associated with the goal.
    
    Args:
        goal: Goal instance to associate interpretation with
        raw_text: Raw goal text to interpret
        db: Database session for persistence
        
    Returns:
        GoalInterpretation: Persisted interpretation record
    """
    interpretation = interpret_goal(raw_text)
    
    interpretation_payload = interpretation.model_dump()
    
    goal_interpretation = GoalInterpretation(
        goal_id=goal.id,
        interpretation_payload=interpretation_payload
    )
    
    db.add(goal_interpretation)
    db.flush()
    
    return goal_interpretation

