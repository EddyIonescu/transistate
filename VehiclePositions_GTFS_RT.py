# add vehicles-transistate table based on all gtfs-rt feeds

from google.transit import gtfs_realtime_pb2
import requests
import pymongo

def getEndpoints():
    getVehiclePositions("http://192.237.29.212:8080/gtfsrealtime/VehiclePositions")

def getVehiclePositions(link):
    feed = gtfs_realtime_pb2.FeedMessage()
    try:
        response = requests.get(link)
        feed.ParseFromString(response.content)
        return feed.entity
    except:
        return []

def main():
    # get list of requests to make from mongodb

