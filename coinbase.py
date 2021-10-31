import requests
#import cbpro
# c = cbpro.PublicClient()

# def GetPair(value1, value2):
#     if value2.upper() == "USDT": value2 = "USD"
#     return value1.upper() + "-" + value2.upper()

# def GetPairPrice(pair):
#     resp = requests.get('https://api.coinbase.com/v2/prices/' + pair + '/buy')

#     return float(resp.json()['data']['amount'])

# def GetBids(pair):
#     order_book = c.get_product_order_book(pair, 3)
#     if len(order_book) < 2:
#         return []

#     bids = order_book["bids"]
    

#     bids_converted = []
#     for element in bids:
#         a = [float(element[0]), float(element[1])]

#         bids_converted.append(a)

#     return bids_converted

# def GetAsks(pair):
#     order_book = c.get_product_order_book(pair, 3)
#     asks = order_book["asks"]

#     asks_converted = []
#     for element in asks:
#         a = [float(element[0]), float(element[1])]
#         asks_converted.append(a)

#     return asks_converted