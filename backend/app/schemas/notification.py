from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class NotificationBase(BaseModel):
    title: str
    body: str
    is_read: bool = False


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    is_read: Optional[bool] = None


class NotificationRead(NotificationBase):
    id: int
    recipient_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
