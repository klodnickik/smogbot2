from sqlalchemy import create_engine
from config import Config
from app import models, crud
from app.models import Station
from app.api import apiClass

stations =[]

print ("Start application")

crud.recreate_database()

s = crud.Session()

station_list = apiClass.getListOfStation()

s.add_all(station_list)
s.commit()


print ("Display list")

print(s.query(Station).all())



s.close()