from sqlalchemy import create_engine
from config import Config
from app import models
from app.models import Base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = Config.DATABASE_URI
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)

def recreate_database():
    print ("Recreate database")
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


