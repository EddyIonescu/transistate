# add transistate table based on all gtfs-rt feeds

from google.transit import gtfs_realtime_pb2
import requests

def getVehiclePositions(link):
    feed = gtfs_realtime_pb2.FeedMessage()
    try:
        response = requests.get(link)
        feed.ParseFromString(response.content)
        return feed.entity
    except:
        return []


