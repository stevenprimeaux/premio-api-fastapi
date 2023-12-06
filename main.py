from fastapi import FastAPI
import actions, schemas

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.get("/movies")
def get_movies() -> list[schemas.Movie]:
    return actions.get_movies()

@app.get("/nominations")
def get_nominations() -> list[schemas.Nomination]:
    return actions.get_nominations()
