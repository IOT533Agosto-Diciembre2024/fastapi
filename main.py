from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

from db_manager import SessionLocal, Director, Ads1115

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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


@app.get("/ads1115")
async def get_data(db: Session = Depends(get_db)):
    data = db.query(Ads1115).all()
    return data
