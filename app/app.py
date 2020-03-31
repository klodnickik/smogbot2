from sqlalchemy import create_engine
from config import Config
from app import models, crud
from app.models import Station, TmpStation
from app.api import apiClass
import logging



stations =[]
logger = logging.getLogger('smogbot')


def refreshTmpListofStations():

    logger.debug ("Open DB session")
    s = crud.Session()

    logger.debug("Pull list of station via API")
    station_list = apiClass.getListOfStation()

    logger.info ("Information uploaded about {} stations".format(len(station_list)))

    s.query(TmpStation).delete()
    s.add_all(station_list)
    s.commit


    logging.debug ("Number of stations in Tmp database: {}".format(s.query(TmpStation).count()))
    logger.debug("Close DB session")
    s.close()




def updateListOfStation():

    logger.debug ("Open DB session")
    s = crud.Session()


    stations_from_tmp = s.query(TmpStation).all()
    stations_from_main = s.query(Station).all()

    logging.debug("Summary before update of Station table. Stations in tmp: {}, station in db: {}".format(len(stations_from_tmp), len(stations_from_main)))

    add_row = True

    for _tmp in stations_from_tmp:
        add_row = True
        for _main in stations_from_main:

            if _tmp.stationName == _main.stationName: add_row = False

        if add_row == True:
            logging.warning("Adding station {}, id: {}".format(_tmp.stationName, _tmp.id))
            c1 = Station(id=_tmp.id, stationName=_tmp.stationName, gegrLat=_tmp.gegrLat, gegrLon=_tmp.gegrLon, cityId=_tmp.cityId, cityName=_tmp.cityName, \
            communeName=_tmp.communeName, districtName=_tmp.districtName, provinceName=_tmp.provinceName, addressStreet=_tmp.addressStreet)
            s.add(c1)
    
        s.commit


    logging.debug ("Number of stations in main table: {}".format(s.query(Station).count()))
    logger.debug("Close DB session")
    s.close()


def DisplayListOfStation():

    print ("Dpsialy")
    s = crud.Session()

    _list_of_station = s.query(Station).order_by(Station.updated_at.asc()).all()

    for _station in _list_of_station:
        print ("stationName: {}, cityName: {}, Updated at: {}".format(_station.stationName, _station.cityName, _station.updated_at))

    print(len(_list_of_station))

    
    s.close()



def DeleteStation(station_name):

    s = crud.Session()
    logging.warning("Request to delete station: {}".format(station_name))
    logging.debug( "Number of stations before deletion: {}".format(s.query(Station).count()))

    station_for_deletion = s.query(Station).filter_by(stationName=station_name).all()

    if len(station_for_deletion) > 0: 
        s.query(Station).filter_by(stationName=station_name).delete()

    logging.warning("Deleted station: {}".format(station_for_deletion))
    logging.debug ("Number of stations after deletion: {}".format(s.query(Station).count()))
    s.commit()
    s.close()



def main():
    logger.warning('Starting application...')

    # this is to refresh list of station in Tmp table
    #refreshTmpListofStations()

    # This is to compare copy content of TMP table to main list of Stations
    updateListOfStation()


    #DisplayListOfStation()
    #updateListOfStation()
    #DeleteStation("Oława - Żołnierzy AK")




if __name__ == "__main__":
    main()

main()