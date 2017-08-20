import configparser
from pymongo import MongoClient
import time
import math
import json

def getAuth():
    config = configparser.ConfigParser()
    config.read("keys")
    config = (config["mongo"]["username"], config["mongo"]["password"])
    return config

def connect():
    auth = getAuth()
    client = MongoClient('mongodb://' + auth[0] + ':' + auth[1] + '@54.183.239.250')
    db = client.transistate
    return db

def vehicleAsMap(vehicle, agency):
    return {
        "agency": agency,
        "tripId": vehicle.trip.trip_id,
        "location": {
            "type": "Point",
            "coordinates": [vehicle.position.longitude, vehicle.position.latitude],
        },
        "timestamp": vehicle.timestamp,
        "vehicle": {
            "id": vehicle.vehicle.id,
            "label": vehicle.vehicle.label,
        }
    }

def insertVehicles(vehicles, agency):
    if len(vehicles):
        db = connect()
        vehicles = [vehicleAsMap(v.vehicle, agency) for v in vehicles]
        timeName = str(math.floor(time.time()))
        collection = db[timeName]
        return collection.insert_many(vehicles)
