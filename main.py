from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from db_manager import SessionLocal, Director

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DirectorDTO(BaseModel):
    name: str
    director_no: int


@app.get("/directors")
async def root(db: Session = Depends(get_db)):
    return db.query(Director).all()


@app.post("/director")
async def save_director(director: DirectorDTO, db: Session = Depends(get_db)):
    director = Director(director_no=director.director_no, director_name=director.name)
    db.add(director)
    db.commit()
    return {"message": "Director Saved"}
