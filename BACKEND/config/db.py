from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATEBASE_URL= "mysql+pymysql://root:1234@localhost:3307/test"
engine = create_engine(SQLALCHEMY_DATEBASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()