import requests

def GetPair(value1, value2):
    if value2.upper() == "USDT" or value2.upper() == "USDC": value2 = "USD"
    if value1.upper() == "ETH": value1 = "XETHZ"
    return value1.upper() + value2.upper()

def PairAvailable(pair):
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair='+ pair)
    if(resp.json().get("error") != []):
        return False
    else:
        return True

def GetPairPrice(pair):
    resp = requests.get('https://api.kraken.com/0/public/Ticker?pair=' + pair)
    if resp.json().get("error") != []:
        return 0.0
    return float(resp.json()["result"][pair]["c"][0])

def GetBids(pair):
    resp = requests.get('https://api.kraken.com/0/public/Depth?pair=' + pair)
    if PairAvailable(pair):
        bids = resp.json()["result"][pair]["bids"]
        bids_converted = []
        for element in bids:
            a = [float(element[0]), float(element[1])]

            bids_converted.append(a)

        return bids_converted
    else:
        return []

def GetAsks(pair):
    resp = requests.get('https://api.kraken.com/0/public/Depth?pair=' + pair)
    if resp.json().get("error") == []:
        asks = resp.json()["result"][pair]["asks"]

        asks_converted = []
        for element in asks:
            a = [float(element[0]), float(element[1])]

            asks_converted.append(a)

        return asks_converted
    else:
        return []
