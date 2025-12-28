from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.db.session import get_db
from app.db.models import Goal, AuditLog
from app.schemas.goal import GoalCreateRequest, GoalCreateResponse, GoalResponse

router = APIRouter()

SYSTEM_USER_ID = UUID("00000000-0000-0000-0000-000000000001")


@router.get("/goals", response_model=List[GoalResponse])
def get_goals(
    db: Session = Depends(get_db)
) -> List[GoalResponse]:
    goals = db.query(Goal).filter(Goal.user_id == SYSTEM_USER_ID).all()
    return [
        GoalResponse(
            goal_id=goal.id,
            raw_text=goal.raw_text,
            created_at=goal.created_at
        )
        for goal in goals
    ]


@router.post("/goals", response_model=GoalCreateResponse, status_code=201)
def create_goal(
    request: GoalCreateRequest,
    db: Session = Depends(get_db)
) -> GoalCreateResponse:
    goal = Goal(
        user_id=SYSTEM_USER_ID,
        raw_text=request.raw_text
    )
    db.add(goal)
    db.flush()

    audit_log = AuditLog(
        entity_type="goal",
        entity_id=goal.id,
        action="CREATE",
        context={"raw_text_length": len(request.raw_text)}
    )
    db.add(audit_log)
    db.flush()

    return GoalCreateResponse(
        goal_id=goal.id,
        created_at=goal.created_at
    )

