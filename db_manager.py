from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://profe:andrestorres@10.48.209.159/proyecto_xrover"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Director(Base):
    __tablename__ = "directors"
    director_no = Column(Integer, primary_key=True, index=True)
    director_name = Column(String(255))


class Ads1115(Base):
    __tablename__ = "ads1115"
    id = Column(Integer, primary_key = True, index=True)
    analog_value = Column(Float)
    voltage = Column(Float)
    fecha = Column(DateTime)

