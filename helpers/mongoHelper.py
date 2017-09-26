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
    client = MongoClient('mongodb://' + auth[0] + ':' + auth[1] + '@54.183.241.195')
    db = client.transistate
    return db


def vehicleAsMap(vehicle, timeName):
    return {
        "trip_id": vehicle.trip.trip_id,
        "route_id": vehicle.trip.route_id,
        "current_status": vehicle.current_status,
        "current_stop_sequence": vehicle.current_stop_sequence,
        "stop_id": vehicle.stop_id,
        "location": {
            # GeoJson for mongo - https://docs.mongodb.com/manual/reference/geojson/#geojson-point
            "type": "Point",
            "coordinates": [vehicle.position.longitude, vehicle.position.latitude],
        },
        "vehicle_timestamp": vehicle.timestamp,
        "vehicle_id": vehicle.vehicle.id,
        "vehicle_label": vehicle.vehicle.label,
        "created_at": timeName,
    }


def insertVehicles(vehicles, agency, timeName):
    logging.info(vehicles)
    logging.info(agency)
    logging.info(timeName)
    if len(vehicles):
        db = connect()
        vehicles = [vehicleAsMap(v.vehicle, agency, timeName) for v in vehicles]
        return db[agency].insert_many(vehicles)
