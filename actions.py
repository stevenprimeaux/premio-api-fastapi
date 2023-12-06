from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Award, Movie, Nomination
from database import engine

def get_movies():
    with Session(engine) as session:
        return session.execute(select(
            Movie.title
        ).limit(10))

def get_nominations():
    with Session(engine) as session:
        return session.execute(select(
            Nomination.year,
            Award.name.label("award"),
            Movie.title.label("movie"),
            Award.country_awarding,
            Nomination.country_submitting
        )
        .join(Nomination.award)
        .join(Nomination.movie)
        .limit(10))