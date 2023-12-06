from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL="postgresql://postgres:postgres@localhost:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
