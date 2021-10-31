import requests

def GetPair(value1, value2):
    if value2.upper() == "USDT" or value2.upper() == "USDC": value2 = "USD"
    return value1.upper() + "-" + value2.upper()

def GetBids(pair):
    resp = requests.get('https://api.dydx.exchange/v3/orderbook/' + pair)
    if resp.json().get("errors") == None:
        bids = resp.json()["bids"]

        bids_converted = []
        for element in bids:
            a = [float(element["price"]), float(element["size"])]

            bids_converted.append(a)
        print(bids_converted)
        return bids_converted
    else:
        return []

def GetAsks(pair):
    resp = requests.get('https://api.dydx.exchange/v3/orderbook/' + pair)
    if resp.json().get("errors") == None:
        asks = resp.json()["asks"]

        asks_converted = []
        for element in asks:
            a = [float(element["price"]), float(element["size"])]

            asks_converted.append(a)

        return asks_converted
    else:
        return []

