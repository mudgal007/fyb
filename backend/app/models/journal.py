from __future__ import annotations

from sqlalchemy import Float, ForeignKey, JSON, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    day_rating: Mapped[float] = mapped_column(Float, default=0.0)
    reflections: Mapped[dict] = mapped_column(JSON, default=dict)
    gratitude: Mapped[str | None] = mapped_column(Text)
    highlights: Mapped[str | None] = mapped_column(Text)
    feelings: Mapped[str | None] = mapped_column(Text)
    paint_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship(back_populates="journal_entries")


from .user import User  # noqa: E402  isort: skip
