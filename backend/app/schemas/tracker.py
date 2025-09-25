from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.tracker import TrackerType


class TrackerItemBase(BaseModel):
    title: str
    item_type: TrackerType
    details: Optional[str] = None
    amount: Optional[float] = None
    is_complete: bool = False


class TrackerItemCreate(TrackerItemBase):
    pass


class TrackerItemUpdate(BaseModel):
    title: Optional[str] = None
    item_type: Optional[TrackerType] = None
    details: Optional[str] = None
    amount: Optional[float] = None
    is_complete: Optional[bool] = None


class TrackerItemRead(TrackerItemBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
