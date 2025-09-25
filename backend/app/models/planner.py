from __future__ import annotations

from enum import Enum
from typing import Optional

from sqlalchemy import Enum as SqlEnum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class PlannerType(str, Enum):
    PRIORITY = "priority"
    ERRAND = "errand"
    SELF_CARE = "self_care"
    WORK = "work"
    CHECKLIST = "checklist"
    EVENT = "event"


class PlannerItem(Base):
    __tablename__ = "planner_items"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    planner_date: Mapped[str] = mapped_column(String(20), nullable=False)
    item_type: Mapped[PlannerType] = mapped_column(SqlEnum(PlannerType), nullable=False)
    is_complete: Mapped[bool] = mapped_column(default=False)
    metadata: Mapped[dict | None] = mapped_column(nullable=True)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship("User")


from .user import User  # noqa: E402  isort: skip
