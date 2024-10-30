from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:andrestorres@localhost/videos"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"
    director_no = Column(Integer, primary_key=True, index=True)
    director_name = Column(String(255))
