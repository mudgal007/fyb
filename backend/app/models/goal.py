from __future__ import annotations

from enum import Enum
from typing import Optional

from sqlalchemy import Enum as SqlEnum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class GoalCategory(str, Enum):
    WORK = "work"
    FAMILY = "family"
    SOCIAL = "social"
    PERSONAL = "personal"
    HEALTH = "health"
    FINANCE = "finance"
    HAPPINESS = "happiness"


class GoalTimeframe(str, Enum):
    DECADE = "10-year"
    FIVE_YEAR = "5-year"
    YEAR = "1-year"
    QUARTER = "quarter"
    MONTH = "month"


class GoalStatus(str, Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"


class Goal(Base):
    __tablename__ = "goals"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    category: Mapped[GoalCategory] = mapped_column(SqlEnum(GoalCategory), nullable=False)
    timeframe: Mapped[GoalTimeframe] = mapped_column(SqlEnum(GoalTimeframe), nullable=False)
    status: Mapped[GoalStatus] = mapped_column(SqlEnum(GoalStatus), default=GoalStatus.NOT_STARTED)
    progress: Mapped[float] = mapped_column(Float, default=0.0)
    target_month: Mapped[int | None] = mapped_column(Integer, nullable=True)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship(back_populates="goals")


from .user import User  # noqa: E402  isort: skip
