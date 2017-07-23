import configparser

def getTransitFeedsKey():
    config = configparser.ConfigParser()
    config.read("keys")
    return config.get("transitfeeds.com", "key")

def main():
    transiFeedKey = getTransitFeedsKey()
    print(transiFeedKey)

main()