from __future__ import annotations

from sqlalchemy import ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class CommunityPost(Base):
    __tablename__ = "community_posts"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    tags: Mapped[list[str]] = mapped_column(JSON, default=list)

    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["User"] = relationship("User")


class CommunityEvent(Base):
    __tablename__ = "community_events"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    event_date: Mapped[str] = mapped_column(String(50), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)

    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    creator: Mapped["User"] = relationship("User")


from .user import User  # noqa: E402  isort: skip
