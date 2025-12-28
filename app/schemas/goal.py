from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class GoalCreateRequest(BaseModel):
    raw_text: str = Field(..., min_length=1)


class GoalCreateResponse(BaseModel):
    goal_id: UUID
    created_at: datetime


class GoalResponse(BaseModel):
    goal_id: UUID
    raw_text: str
    created_at: datetime

