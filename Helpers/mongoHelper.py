import configparser

import logging
from pymongo import MongoClient

def getAuth():
    config = configparser.ConfigParser()
    config.read("keys")
    config = (config["mongo"]["username"], config["mongo"]["password"])
    return config


def connect():
    auth = getAuth()
    client = MongoClient('mongodb://' + auth[0] + ':' + auth[1] + '@172.31.11.38')
    db = client.transistate
    return db


def vehicleAsMap(vehicle, agency):
    return {
        "agency": agency,
        "trip_id": vehicle.trip.trip_id,
        "location": {
            # GeoJson for mongo - https://docs.mongodb.com/manual/reference/geojson/#geojson-point
            "type": "Point",
            "coordinates": [vehicle.position.longitude, vehicle.position.latitude],
        },
        "timestamp": vehicle.timestamp,
        "vehicle_id": vehicle.vehicle.id,
        "vehicle_label": vehicle.vehicle.label,
    }


def insertVehicles(vehicles, agency, timeName):
    logging.info(vehicles)
    logging.info(agency)
    logging.info(timeName)
    if len(vehicles):
        db = connect()
        vehicles = [vehicleAsMap(v.vehicle, agency) for v in vehicles]
        collection = db[timeName]
        return collection.insert_many(vehicles)
