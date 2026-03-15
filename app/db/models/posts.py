from sqlalchemy import Text, Date, Index, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.enums.source_enum import SourceEnum


class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(
        Text, 
        nullable=False
        )
    link: Mapped[str | None] = mapped_column(
        Text, 
        nullable=True
        )
    source: Mapped[SourceEnum] = mapped_column(
        Enum(SourceEnum, name="source_enum"),
        nullable=False
        )
    date: Mapped[Date] = mapped_column(
        Date, 
        nullable=False, 
        index=True
        )