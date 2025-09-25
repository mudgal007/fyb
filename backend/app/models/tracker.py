from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SqlEnum, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class TrackerType(str, Enum):
    GOAL = "goal"
    TODO = "todo"
    APPOINTMENT = "appointment"
    SHOPPING = "shopping"
    BUDGET = "budget"


class TrackerItem(Base):
    __tablename__ = "tracker_items"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    item_type: Mapped[TrackerType] = mapped_column(SqlEnum(TrackerType), nullable=False)
    details: Mapped[str | None] = mapped_column(Text)
    amount: Mapped[float | None] = mapped_column(Float)
    is_complete: Mapped[bool] = mapped_column(default=False)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship("User")


from .user import User  # noqa: E402  isort: skip
