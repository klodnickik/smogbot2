import requests
from app.models import TmpStation

class apiClass():
    def getListOfStation():
        station_list = []

        print("Pobieram przez API liste stacji pomiarowych")
        endpoint = 'https://api.gios.gov.pl/pjp-api/rest/station/findAll'
        json_output = requests.get(endpoint).json()


        for station in json_output:
            stationObj = TmpStation (
                id = station["id"], 
                stationName = station["stationName"],
                gegrLat = station["gegrLat"],
                gegrLon = station["gegrLon"],
                cityId = station["city"]["id"],
                cityName = station["city"]["name"],
                communeName = station["city"]["commune"]["communeName"],
                districtName = station["city"]["commune"]["districtName"],
                provinceName = station["city"]["commune"]["provinceName"],
                addressStreet = station["addressStreet"] 
            )
            station_list.append(stationObj)

        return station_list


