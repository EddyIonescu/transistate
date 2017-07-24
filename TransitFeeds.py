# Get list of GTFS-RT vehicle-position feeds from TransitFeeds and save it in mongodb

import configparser
import requests
import pymongo

def getTransitFeedsKey():
    config = configparser.ConfigParser()
    config.read("keys")
    return config.get("transitfeeds.com", "key")

def getFeeds():
    response = requests.get(

def saveFeeds():


def main():
    transiFeedKey = getTransitFeedsKey()


main()