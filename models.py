import uuid
from typing import Optional

from sqlalchemy import text, ForeignKey, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Award(Base):
    __tablename__ = "award"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    id_institution: Mapped[uuid.UUID] = mapped_column(ForeignKey("institution.id"))
    name: Mapped[str]
    country_awarding: Mapped[Optional[str]]
    nominations: Mapped[list["Nomination"]] = relationship(back_populates="award")

class Institution(Base):
    __tablename__ = "institution"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    name: Mapped[str]

class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    title: Mapped[str]
    nominations: Mapped[list["Nomination"]] = relationship(back_populates="movie")
    # imdb_id

class Nomination(Base):
    __tablename__ = "nomination"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    year: Mapped[int]
    id_award: Mapped[uuid.UUID] = mapped_column(ForeignKey("award.id"))
    id_movie: Mapped[uuid.UUID] = mapped_column(ForeignKey("movie.id"))
    country_submitting: Mapped[Optional[str]]
    award: Mapped["Award"] = relationship(back_populates="nominations")
    movie: Mapped["Movie"] = relationship(back_populates="nominations")
