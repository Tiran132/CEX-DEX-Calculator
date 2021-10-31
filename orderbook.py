import CEX
import DEX

amount = 1000000
token1 = "SUSHI"
token2 = "USDT"
isBuying = False

pairs1 = {
    "SUSHI": ["USDT"],
    "1INCH": ["USDT"],
}

def GetBuyingPrice():
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

def GetSellingPrice():
    cex_selling = CEX.CEXSelling(amount, token1, token2)
    dex_selling = DEX.DEXSelling(amount, token1, token2)
    
    cex_selling.CreateBids()
    dictionary_CEX_Sell = cex_selling.Calculate()

    dex_selling.CreateBids()
    dictionary_DEX_Sell = dex_selling.Calculate()
    
    return {
        "CEX_Buy": dictionary_CEX_Sell,
        "DEX_Buy": dictionary_DEX_Sell,
    }




if isBuying:
    print(GetBuyingPrice())
else:
    print(GetSellingPrice())








# cex_buying = CEX.CEXBuying(amount, token1, token2)
# dex_buy = DEX.DEXBuying(amount, token1, token2)



# while True:
#     cex_buying.amount = amount
#     dex_buy.amount = amount
#     cex_buying.CreateAsks()
    
#     dictionary_CEX_Buy = cex_buying.Calculate()

#     # CEX.
#     print("\n\nCEX\nExpected Price: ",  dictionary_CEX_Buy["expected_price"])
#     print("Real Exchenge Price: ", dictionary_CEX_Buy["real_exchenged_price"])

#     if dictionary_CEX_Buy["end_amount"] > 0:
#         print("End Amount: ", dictionary_CEX_Buy["end_amount"])
    
#     print("Delta: ", dictionary_CEX_Buy["delta_in_percents"])

#     #DEX
#     dex_buy.CreateAsks()
    
#     dictionary = dex_buy.Calculate()
#     print("\n\nDEX\nExpected Price: ",  dictionary["expected_price"])
#     print("Real Exchenge Price: ", dictionary["real_exchenged_price"])

#     if dictionary["end_amount"] > 0:
#         print("End Amount: ", dictionary["end_amount"])
    
#     print("Delta: ", dictionary["delta_in_percents"])



















# while True:
#     cex1.amount = amount
#     dex1.amount = amount
#     cex1.CreateBids()
#     dex1.CreateBids()
    
#     dictionary_CEX = cex1.Calculate()
#     dictionary_DEX = dex1.Calculate()

#     # CEX.

#     print("\nCEX\nExpected Price: ",  dictionary_CEX["expected_price"])
#     print("Real Exchenge Price: ", dictionary_CEX["real_exchenged_price"])

#     if dictionary_CEX["end_amount"] > 0:
#         print("End Amount: ", dictionary_CEX["end_amount"])
    
#     print("Delta: ", dictionary_CEX["delta_in_percents"])

#     # DEX.

#     print("\nDEX\n")
#     print("Real Exchenge Price: ", dictionary_DEX["real_exchenged_price"])

#     if dictionary_CEX["end_amount"] > 0:
#         print("End Amount: ", dictionary_DEX["end_amount"])
    
#     print("Delta: ", dictionary_DEX["delta_in_percents"])


#     # Main Delta.
#     print("\n\nDelta of deltas: ",  dictionary_CEX["delta_in_percents"] - dictionary_DEX["delta_in_percents"], "\n#################################\n")

#     # amount += 100000

