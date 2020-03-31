from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float, TIMESTAMP
from datetime import datetime

Base = declarative_base()

class Station(Base):
    __tablename__ = 'station'
    id = Column(Integer, primary_key=True)
    stationName = Column(String(128))
    gegrLat = Column(Float)
    gegrLon = Column(Float)
    cityId = Column(Integer)
    cityName = Column(String(64))
    communeName = Column(String(64))
    districtName = Column(String(64))
    provinceName = Column(String(64))
    addressStreet = Column(String(64))
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return "<Station(stationName='{}', cityName='{}', communeName={}, provinceName={}, updated_at={})>"\
                .format(self.stationName, self.cityName, self.communeName, self.provinceName, self.updated_at)


class TmpStation(Base):
    __tablename__ = 'tmp_station'
    id = Column(Integer, primary_key=True)
    stationName = Column(String(128))
    gegrLat = Column(Float)
    gegrLon = Column(Float)
    cityId = Column(Integer)
    cityName = Column(String(64))
    communeName = Column(String(64))
    districtName = Column(String(64))
    provinceName = Column(String(64))
    addressStreet = Column(String(64))
    updated_at = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return "<Station(stationName='{}', cityName='{}', communeName={}, provinceName={}, updated_at={})>"\
                .format(self.stationName, self.cityName, self.communeName, self.provinceName, self.updated_at)