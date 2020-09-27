import http.client
import mimetypes
import json
from distanceRequest import getDistance
def getHospList(latitude, longitude):
    """
    Prints a list of tuples of length 5, with the formatted addresses of nearby hospitals, distance by car, time to travel by car, all as strings
    """
    conn = http.client.HTTPSConnection("api.radar.io")
    payload = ''
    headers = {
      'Authorization': 'prj_test_pk_6e76504d47441be5e8ad2fc0dcd6daaa57083aa5 '
    }


    conn.request("GET", "/v1/search/autocomplete?query=hospital&near=" + str(latitude) + "," + str(longitude) + "&limit=5", payload, headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")


    json_data = json.loads(data)

    #print(json_data)
    addresses = json_data["addresses"]

    d_list = []

    formatted_address_list = []
    for address in addresses:
        hospital_place = address["formattedAddress"]
        a = hospital_place.find(",")
        formatted_address_list.append((hospital_place[0:a], getDistance(latitude, longitude, address["latitude"], address["longitude"])[0], getDistance(latitude, longitude, address["latitude"], address["longitude"])[1]))
        #d_list.append((address["latitude"],address["longitude"]))


    #print(d_list)
    #print(formatted_address_list)
    return formatted_address_list
