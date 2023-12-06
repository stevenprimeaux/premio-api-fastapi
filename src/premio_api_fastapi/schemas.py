from typing import Optional
from pydantic import BaseModel


class Award(BaseModel):
    institution: str
    name: str
    country_awarding: str

    class Config:
        from_attributes = True


class Institution(BaseModel):
    name: str

    class Config:
        from_attributes = True


class Movie(BaseModel):
    title: str

    class Config:
        from_attributes = True


class Nomination(BaseModel):
    year: int
    award: str
    movie: str
    country_awarding: Optional[str]
    country_submitting: Optional[str]

    class Config:
        from_attributes = True
