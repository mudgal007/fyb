from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.habit import HabitFrequency


class HabitBase(BaseModel):
    title: str
    description: Optional[str] = None
    frequency: HabitFrequency = HabitFrequency.DAILY
    streak: int = 0
    target: int = 1


class HabitCreate(HabitBase):
    pass


class HabitUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    frequency: Optional[HabitFrequency] = None
    streak: Optional[int] = None
    target: Optional[int] = None


class HabitRead(HabitBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
