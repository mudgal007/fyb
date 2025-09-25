from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel


class JournalBase(BaseModel):
    day_rating: float = 0.0
    reflections: dict[str, Any] = {}
    gratitude: Optional[str] = None
    highlights: Optional[str] = None
    feelings: Optional[str] = None
    paint_data: Optional[dict[str, Any]] = None


class JournalCreate(JournalBase):
    pass


class JournalUpdate(BaseModel):
    day_rating: Optional[float] = None
    reflections: Optional[dict[str, Any]] = None
    gratitude: Optional[str] = None
    highlights: Optional[str] = None
    feelings: Optional[str] = None
    paint_data: Optional[dict[str, Any]] = None


class JournalRead(JournalBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
