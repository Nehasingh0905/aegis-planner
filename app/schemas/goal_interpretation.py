from pydantic import BaseModel
from typing import List, Optional


class GoalInterpretation(BaseModel):
    objective: str
    time_horizon: Optional[str]
    constraints: List[str]
    assumptions: List[str]
    ambiguities: List[str]
    risk_flags: List[str]

