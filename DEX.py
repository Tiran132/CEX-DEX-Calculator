import Dydx
import QuickSort
import BinanceBid

class DEXSelling():
    def CreateBids(self):
        value1 = self.token1
        value2 = self.token2

        bids_Dydx = Dydx.GetBids(Dydx.GetPair(value1, value2))

        self.bids = bids_Dydx
        QuickSort.Bubble_sort(self.bids)
        return self.bids
    
    def Calculate(self):
        s = 0
        amount = self.amount
        firstAmount = amount
        expPrice = self.GetExpectedPrice()
        kurs = self.GetPairPrice()

        expPrice = self.GetExpectedPrice()
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
            
        if expPrice > 0:
            return {
                "real_exchanged_price": s,
                "end_amount": amount,
                "delta_in_percents": 100 - (100 * s / expPrice)
            }
        else:
            return {
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
        
class DEXBuying():
    def CreateAsks(self):
        value1 = self.token1
        value2 = self.token2

        asks_Dydx = Dydx.GetAsks(Dydx.GetPair(value1, value2))

        self.asks = asks_Dydx
        QuickSort.Bubble_sort1(self.asks)
        return self.asks

    def Calculate(self):
        s = 0
        amount = self.amount

        for element in self.asks:
            ask_Price = element[0]
            ask_Volume = element[1]
            if (amount - ask_Volume > 0):
                amount -= ask_Volume
                s += ask_Price * ask_Volume
            else:
                s += ask_Price * amount
                amount = 0
                break
        expPrice = self.GetExpectedPrice()
        if expPrice > 0:
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
        self.asks = []

