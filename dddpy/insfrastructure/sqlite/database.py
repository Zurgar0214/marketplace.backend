from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQL_DATABASE_URL = "sqlite:///marketplace.db"

engine = create_engine(SQL_DATABASE_URL, echo=True)
session = sessionmaker(bind=engine)