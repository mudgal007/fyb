from __future__ import annotations

from enum import Enum
from typing import List

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class UserRole(str, Enum):
    ADMIN = "admin"
    MEMBER = "member"
    COACH = "coach"


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    role: Mapped[UserRole] = mapped_column(default=UserRole.MEMBER)

    goals: Mapped[List["Goal"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    habits: Mapped[List["Habit"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    mood_entries: Mapped[List["MoodEntry"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    journal_entries: Mapped[List["JournalEntry"]] = relationship(back_populates="owner", cascade="all, delete-orphan")
    notifications: Mapped[List["Notification"]] = relationship(back_populates="recipient", cascade="all, delete-orphan")


from .goal import Goal  # noqa: E402  isort: skip
from .habit import Habit  # noqa: E402  isort: skip
from .mood import MoodEntry  # noqa: E402  isort: skip
from .journal import JournalEntry  # noqa: E402  isort: skip
from .notification import Notification  # noqa: E402  isort: skip
