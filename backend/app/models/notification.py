from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Notification(Base):
    __tablename__ = "notifications"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    is_read: Mapped[bool] = mapped_column(Boolean, default=False)

    recipient_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    recipient: Mapped["User"] = relationship(back_populates="notifications")


from .user import User  # noqa: E402  isort: skip
