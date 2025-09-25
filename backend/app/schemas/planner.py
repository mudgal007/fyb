from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel

from app.models.planner import PlannerType


class PlannerItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    planner_date: str
    item_type: PlannerType
    is_complete: bool = False
    metadata: Optional[dict[str, Any]] = None


class PlannerItemCreate(PlannerItemBase):
    pass


class PlannerItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    planner_date: Optional[str] = None
    item_type: Optional[PlannerType] = None
    is_complete: Optional[bool] = None
    metadata: Optional[dict[str, Any]] = None


class PlannerItemRead(PlannerItemBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
