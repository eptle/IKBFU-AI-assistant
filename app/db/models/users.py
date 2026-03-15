import enum
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(
        BigInteger, 
        unique=True, 
        nullable=False,
        index=True
        )
    username: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
        )
    first_name: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
        )
    last_name: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
        )
    is_admin: Mapped[bool] = mapped_column(
        Boolean, 
        default=False
        )
    is_banned: Mapped[bool] = mapped_column(
        Boolean, 
        default=False
        )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow
        )