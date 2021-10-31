import requests


def GetPair(value1, value2):

    return value1.upper() + value2.upper()

def GetPairPrice(pair):
    resp = requests.get("https://api.binance.com/api/v3/ticker/price", params=dict(symbol=pair))

    if(resp.json().get("msg") == None):
        return float(resp.json()["price"])
    else:
        return 0.0


def GetBids(pair):
    resp = requests.get("https://api.binance.com/api/v3/depth", params=dict(symbol=pair))
    if(resp.json().get("msg") == None):
        bids = resp.json()["bids"]

        bids_converted = []
        for element in bids:
            a = [float(element[0]), float(element[1])]

            bids_converted.append(a)

        return bids_converted
    else:
        return []

def GetAsks(pair):
    resp = requests.get("https://api.binance.com/api/v3/depth", params=dict(symbol=pair))
    if(resp.json().get("msg") == None):
        asks = resp.json()["asks"]

        asks_converted = []
        for element in asks:
            a = [float(element[0]), float(element[1])]
            asks_converted.append(a)

        return asks_converted
    else:
        return []

