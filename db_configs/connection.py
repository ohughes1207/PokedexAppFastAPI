from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = "postgresql://pokedexdb_lsx3_user:FkkwMmVfD185SnzAIHD0Vr3wQFsd0w79@dpg-cimnjo5gkuvgvh9vpevg-a.frankfurt-postgres.render.com/pokedexdb_lsx3"

engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()