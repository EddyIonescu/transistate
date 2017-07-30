import requests
import configparser
from pymongo import MongoClient

def getAuth():
    config = configparser.ConfigParser()
    config.read("mongo")
    return (config.get("mongo", "username"), config.get("mongo", "password"))

def connect():
    client = MongoClient()

