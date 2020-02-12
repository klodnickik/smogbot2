from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

Base = declarative_base()

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    stationName = Column(String)
    gegrLat = Column(Float)
    gegrLon = Column(Float)
    cityId = Column(Integer)
    cityName = Column(String)
    communeName = Column(String)
    districtName = Column(String)
    provinceName = Column(String)
    addressStreet = Column(String)
    
    def __repr__(self):
        return "<Station(stationName='{}', cityName='{}', communeName={}, provinceName={})>"\
                .format(self.stationName, self.cityName, self.communeName, self.provinceName)