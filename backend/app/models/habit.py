from __future__ import annotations

from enum import Enum
from typing import Optional

from sqlalchemy import Enum as SqlEnum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class HabitFrequency(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    CUSTOM = "custom"


class Habit(Base):
    __tablename__ = "habits"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(512))
    frequency: Mapped[HabitFrequency] = mapped_column(SqlEnum(HabitFrequency), default=HabitFrequency.DAILY)
    streak: Mapped[int] = mapped_column(Integer, default=0)
    target: Mapped[int] = mapped_column(Integer, default=1)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship(back_populates="habits")


from .user import User  # noqa: E402  isort: skip
