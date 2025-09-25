from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.goal import GoalCategory, GoalStatus, GoalTimeframe


class GoalBase(BaseModel):
    title: str
    description: Optional[str] = None
    category: GoalCategory
    timeframe: GoalTimeframe
    status: GoalStatus = GoalStatus.NOT_STARTED
    progress: float = 0.0
    target_month: Optional[int] = None


class GoalCreate(GoalBase):
    pass


class GoalUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[GoalCategory] = None
    timeframe: Optional[GoalTimeframe] = None
    status: Optional[GoalStatus] = None
    progress: Optional[float] = None
    target_month: Optional[int] = None


class GoalRead(GoalBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
