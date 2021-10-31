import Kraken
import BinanceBid
import coinbase
import QuickSort

class CEXSelling():
    def CreateBids(self):
        value1 = self.token1
        value2 = self.token2

        bids_Binance = BinanceBid.GetBids(BinanceBid.GetPair(value1, value2))
        bids_Kraken = Kraken.GetBids(Kraken.GetPair(value1, value2))
        bids_coinbase = []#coinbase.GetBids(coinbase.GetPair(value1, value2))

        self.bids = bids_Binance + bids_coinbase + bids_Kraken
        QuickSort.Bubble_sort(self.bids)
        return self.bids
    
    def Calculate(self):
        s = 0
        amount = self.amount
        firstAmount = amount
        expPrice = self.GetExpectedPrice()
        kurs = self.GetPairPrice()

        for element in self.bids:
            bid_Price = element[0]
            bid_Volume = element[1]

            if (amount - bid_Volume > 0):
                amount -= bid_Volume
                s += bid_Price * bid_Volume
            else:
                s += bid_Price * amount
                amount = 0
                break

        if expPrice != 0:    
            return {
                "expected_price": expPrice,
                "real_exchanged_price": s,
                "end_amount": amount,
                "delta_in_percents": 100 - (100 * s / expPrice)
            }
        else:
            return {
                "expected_price": expPrice,
                "real_exchanged_price": s,
                "end_amount": amount,
                "delta_in_percents":0
            }
    

    def GetPairPrice(self):
        return float(BinanceBid.GetPairPrice(BinanceBid.GetPair(self.token1, self.token2)))
    
    def GetExpectedPrice(self):
        return self.GetPairPrice() * self.amount

    def __init__(self, amount, token1, token2) -> None:
        self.amount = amount
        self.token1 = token1
        self.token2 = token2
        self.bids = []
        
class CEXBuying():
    def CreateAsks(self):
        value1 = self.token1
        value2 = self.token2

        asks_Binance = BinanceBid.GetAsks(BinanceBid.GetPair(value1, value2))
        
        asks_Kraken = Kraken.GetAsks(Kraken.GetPair(value1, value2))
        asks_coinbase = []#coinbase.GetAsks(coinbase.GetPair(value1, value2))

        self.asks = asks_Binance + asks_Kraken + asks_coinbase
        QuickSort.Bubble_sort1(self.asks)
        return self.asks

    def Calculate(self):
        s = 0
        amount = self.amount
        firstAmount = amount

        for element in self.asks:
            asks_Price = element[0]
            asks_Volume = element[1]
            if (amount - asks_Volume > 0):
                amount -= asks_Volume
                s += asks_Price * asks_Volume
            else:
                s += asks_Price * amount
                amount = 0
                break
        expPrice = self.GetExpectedPrice()
        if expPrice > 0:
            kurs = self.GetPairPrice()
            
            if amount > 0:
                return {
                    "expected_price": expPrice,
                    "real_exchanged_price": s,
                    "end_amount": amount,
                    "delta_in_percents": (100 * s / ((firstAmount - amount) * kurs)) - 100
                }
            else:
                return {
                    "expected_price": expPrice,
                    "real_exchanged_price": s,
                    "end_amount": amount,
                    "delta_in_percents": (100 * s / expPrice) - 100
                }
        else:
            return {
                "expected_price": expPrice,
                "real_exchanged_price": s,
                "end_amount": amount,
                "delta_in_percents": 0
            } 
    
    def GetPairPrice(self):
        return float(BinanceBid.GetPairPrice(BinanceBid.GetPair(self.token1, self.token2)))

    def GetExpectedPrice(self):
        return self.GetPairPrice() * self.amount
    
    def __init__(self, amount, token1, token2) -> None:
        self.amount = amount
        self.token1 = token1
        self.token2 = token2
        self.bids = []

