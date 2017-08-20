# Get list of GTFS-RT vehicle-position feeds from TransitFeeds and save it in mongodb


from VehiclePositions_GTFS_RT import getVehiclePositions
from mongo_helper import insertVehicles

#def getTransitFeedsKey():
#    config = configparser.ConfigParser()
#    config.read("keys")
#    return config.get("transitfeeds.com", "key")

# Get the feeds from TransitFeeds
# TODO def getFeeds():

# Cache the feeds (endpoints) in S3
# TODO def saveFeeds():

# Get GTFS-RT endpoints from the Transit Feeds
def getGtfsRtEndpoints():
    return [
        "http://192.237.29.212:8080/gtfsrealtime/VehiclePositions",
        "http://gtfs.translink.ca/gtfsposition?apikey=nVhpsz4sxmabMQRo67eK"
    ]

def getTransistate():
    # transiFeedKey = getTransitFeedsKey()
    endpoints = getGtfsRtEndpoints()
    waterlooData = getVehiclePositions(endpoints[0])
    vancouverData = getVehiclePositions(endpoints[1])
    insertVehicles(waterlooData, "GRT_Waterloo")
    insertVehicles(vancouverData, "Translink_Vancouver")
