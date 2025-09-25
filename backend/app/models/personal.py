from __future__ import annotations

from enum import Enum

from sqlalchemy import Enum as SqlEnum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class PersonalCategory(str, Enum):
    BOOK = "books"
    SKILL = "skills"
    WISHLIST = "wishlist"
    TRAVEL = "travel"
    MOVIE = "movies"
    EVENT = "events"
    PEOPLE = "people"


class PersonalItem(Base):
    __tablename__ = "personal_items"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[PersonalCategory] = mapped_column(SqlEnum(PersonalCategory), nullable=False)
    details: Mapped[str | None] = mapped_column(Text)
    quote: Mapped[str | None] = mapped_column(Text)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship("User")


from .user import User  # noqa: E402  isort: skip
