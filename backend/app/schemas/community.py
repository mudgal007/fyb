from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


class CommunityPostBase(BaseModel):
    title: str
    body: str
    tags: List[str] = []


class CommunityPostCreate(CommunityPostBase):
    pass


class CommunityPostUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    tags: Optional[List[str]] = None


class CommunityPostRead(CommunityPostBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CommunityEventBase(BaseModel):
    name: str
    description: str
    event_date: str
    location: str


class CommunityEventCreate(CommunityEventBase):
    pass


class CommunityEventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    event_date: Optional[str] = None
    location: Optional[str] = None


class CommunityEventRead(CommunityEventBase):
    id: int
    creator_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
