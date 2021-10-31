import CEX
import DEX

def GetBuyingPrice_CEX(token1, token2, amount):
    cex_buying = CEX.CEXBuying(amount, token1, token2)
    
    cex_buying.CreateAsks()
    dictionary_CEX_Buy = cex_buying.Calculate()
    
    return dictionary_CEX_Buy

def GetBuyingPrice_DEX(token1, token2, amount):
    dex_buy = DEX.DEXBuying(amount, token1, token2)

    dex_buy.CreateAsks()
    dictionary_DEX_Buy = dex_buy.Calculate()
    
    return dictionary_DEX_Buy

def GetSellingPrice_CEX(token1, token2, amount):
    cex_sell = CEX.CEXSelling(amount, token1, token2)
    
    cex_sell.CreateBids()
    dictionary_CEX_Sell = cex_sell.Calculate()
    
    return dictionary_CEX_Sell

def GetSellingPrice_DEX(token1, token2, amount):
    dex_sell = DEX.DEXSelling(amount, token1, token2)

    dex_sell.CreateBids()
    dictionary_DEX_Sell = dex_sell.Calculate()
    
    return dictionary_DEX_Sell


def GetBuyingPrice(token1, token2, amount):
    cex_buying = CEX.CEXBuying(amount, token1, token2)
    dex_buy = DEX.DEXBuying(amount, token1, token2)
    
    cex_buying.CreateAsks()
    dictionary_CEX_Buy = cex_buying.Calculate()
    
    dex_buy.CreateAsks()
    dictionary_DEX_Buy = dex_buy.Calculate()
    
    return {
        "CEX_Buy": dictionary_CEX_Buy,
        "DEX_Buy": dictionary_DEX_Buy,
    }

def GetSellingPrice(token1, token2, amount):
    cex_selling = CEX.CEXSelling(amount, token1, token2)
    dex_selling = DEX.DEXSelling(amount, token1, token2)
    
    cex_selling.CreateBids()
    dictionary_CEX_Sell = cex_selling.Calculate()

    dex_selling.CreateBids()
    dictionary_DEX_Sell = dex_selling.Calculate()
    
    return {
        "CEX_Sell": dictionary_CEX_Sell,
        "DEX_Sell": dictionary_DEX_Sell,
    }


def GetDictionary(token1, token2, amount, isBuying = False):
    if isBuying:
        return GetBuyingPrice(token1, token2, amount)
    else:
        return GetSellingPrice(token1, token2, amount)


