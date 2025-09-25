from __future__ import annotations

from sqlalchemy import Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class MoodEntry(Base):
    __tablename__ = "mood_entries"

    mood: Mapped[str] = mapped_column(String(50), nullable=False)
    intensity: Mapped[float] = mapped_column(Float, default=0.5)
    notes: Mapped[str | None] = mapped_column(Text)
    suggestion: Mapped[str | None] = mapped_column(Text)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship(back_populates="mood_entries")


from .user import User  # noqa: E402  isort: skip
