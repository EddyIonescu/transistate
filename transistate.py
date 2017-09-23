# Get list of GTFS-RT vehicle-position feeds from TransitFeeds
# and store it in the database

# TODO fetch realtime endpoints and other agency info using the transiagency service

from helpers.fetchVehiclePositions import getVehiclePositions
from helpers.mongoHelper import insertVehicles

def getGtfsRtEndpoints():
    return [
        "http://192.237.29.212:8080/gtfsrealtime/VehiclePositions",
        "http://gtfs.translink.ca/gtfsposition?apikey=nVhpsz4sxmabMQRo67eK"
    ]

def getTransistate(timeName):
    endpoints = getGtfsRtEndpoints()
    waterlooData = getVehiclePositions(endpoints[0])
    vancouverData = getVehiclePositions(endpoints[1])
    insertVehicles(waterlooData, "GRT_Waterloo", timeName)
    insertVehicles(vancouverData, "Translink_Vancouver", timeName)
