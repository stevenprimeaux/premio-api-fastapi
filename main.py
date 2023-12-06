from fastapi import FastAPI
import actions, schemas

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/awards")
def get_movies() -> list[schemas.Award]:
    return actions.get_awards()

@app.get("/institutions")
def get_movies() -> list[schemas.Institution]:
    return actions.get_institutions()

@app.get("/movies")
def get_movies() -> list[schemas.Movie]:
    return actions.get_movies()

@app.get("/nominations")
def get_nominations(
    country_awarding: str | None = None,
    country_submitting: str | None = None
    ) -> list[schemas.Nomination]:
    return actions.get_nominations(country_awarding, country_submitting)
