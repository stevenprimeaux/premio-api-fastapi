from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Award, Institution, Movie, Nomination
from database import engine

def get_awards():
    with Session(engine) as session:
        return session.execute(select(
            Institution.name.label("institution"),
            Award.name,
            Award.country_awarding
            )
            .join(Award.institution)
            .order_by(Award.name)
            )

def get_institutions():
    with Session(engine) as session:
        return session.execute(
            select(Institution.name).order_by(Institution.name))

def get_movies():
    with Session(engine) as session:
        return session.execute(select(Movie.title).order_by(Movie.title))

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
            .order_by(Award.name, Nomination.year)
            )
