from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.models.personal import PersonalCategory


class PersonalItemBase(BaseModel):
    title: str
    category: PersonalCategory
    details: Optional[str] = None
    quote: Optional[str] = None


class PersonalItemCreate(PersonalItemBase):
    pass


class PersonalItemUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[PersonalCategory] = None
    details: Optional[str] = None
    quote: Optional[str] = None


class PersonalItemRead(PersonalItemBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
