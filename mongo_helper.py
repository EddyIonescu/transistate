import requests
import configparser
from pymongo import MongoClient

def getAuth():
    config = configparser.ConfigParser()
    config.read("mongo")
    return (config.get("mongo", "username"), config.get("mongo", "password"))

def connect():
    auth = getAuth()
    client = MongoClient('mongodb://' + auth[0] + ':' + auth[1] + '@54.183.239.250')
    db = client.transistate
    

