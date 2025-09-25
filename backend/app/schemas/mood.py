from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class MoodBase(BaseModel):
    mood: str
    intensity: float = 0.5
    notes: Optional[str] = None
    suggestion: Optional[str] = None


class MoodCreate(MoodBase):
    pass


class MoodUpdate(BaseModel):
    mood: Optional[str] = None
    intensity: Optional[float] = None
    notes: Optional[str] = None
    suggestion: Optional[str] = None


class MoodRead(MoodBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
