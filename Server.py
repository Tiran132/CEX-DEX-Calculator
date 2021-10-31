import PriceLister
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080

f = open("calculator.html", "r")
htmlPageText = f.read()
f.close()

def Round(num, digits):
    return int(float(num) * 10**digits)/10**digits


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        htmlPageText1 = htmlPageText


        if self.path.find("?") != -1:
            req = self.path.split("?")[1].split("&")
            resp = dict()

            for i in req:
                elements = i.split("=")

                resp[elements[0]] = elements[1]

            
            htmlPageText1 = htmlPageText1.replace("\{\{ result_display \}\}", "block")


            isBuying = False

            if resp["operation"] == "Buy":
                isBuying = True
            
            


            if isBuying:
                prices_Buy = PriceLister.GetBuyingPrice(resp["token1"], resp["token2"], float(resp["amount"]))
                bExpectedPrice = Round(prices_Buy["CEX_Buy"]["expected_price"], 2)
                bRealExchangeCEX = Round(prices_Buy["CEX_Buy"]["real_exchanged_price"], 2)
                bRealExchangeDEX = Round(prices_Buy["DEX_Buy"]["real_exchanged_price"], 2)
                bDeltaPercentCEX = Round(prices_Buy["CEX_Buy"]["delta_in_percents"], 2)
                bDeltaPercentDEX = Round(prices_Buy["DEX_Buy"]["delta_in_percents"], 2)


                htmlPageText1 = htmlPageText1.replace("<!-- {{ token1_name }} -->", resp["token1"])
                htmlPageText1 = htmlPageText1.replace("<!-- {{ token2_name }} -->", resp["token2"])

                htmlPageText1 = htmlPageText1.replace("<!-- {{ exp_price-value }} -->", str(bExpectedPrice))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ real_price-CEX-value }} -->", str(bRealExchangeCEX))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ real_price-DEX-value }} -->", str(bRealExchangeDEX))

                htmlPageText1 = htmlPageText1.replace("<!-- {{ CEX_loss-value }} -->", str(bDeltaPercentCEX))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ DEX_loss-value }} -->", str(bDeltaPercentDEX))


                delta_prices = abs(Round(bRealExchangeCEX - bRealExchangeDEX, 2))
                delta_percents = Round(bDeltaPercentCEX - bDeltaPercentDEX, 2)

                htmlPageText1 = htmlPageText1.replace("<!-- {{ delta_prices }} -->", str(delta_prices))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ delta_percents }} -->", str(delta_percents))
            else:
                prices_Sell = PriceLister.GetSellingPrice(resp["token1"], resp["token2"], float(resp["amount"]))

                sExpectedPrice = Round(prices_Sell["CEX_Sell"]["expected_price"], 2)
                sRealExchangeCEX = Round(prices_Sell["CEX_Sell"]["real_exchanged_price"], 2)
                sRealExchangeDEX = Round(prices_Sell["DEX_Sell"]["real_exchanged_price"], 2)
                sDeltaPercentCEX = Round(prices_Sell["CEX_Sell"]["delta_in_percents"], 2)
                sDeltaPercentDEX = Round(prices_Sell["DEX_Sell"]["delta_in_percents"], 2)
            

                htmlPageText1 = htmlPageText1.replace("<!-- {{ token1_name }} -->", resp["token1"])
                htmlPageText1 = htmlPageText1.replace("<!-- {{ token2_name }} -->", resp["token2"])

                htmlPageText1 = htmlPageText1.replace("<!-- {{ exp_price-value }} -->", str(sExpectedPrice))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ real_price-CEX-value }} -->", str(sRealExchangeCEX))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ real_price-DEX-value }} -->", str(sRealExchangeDEX))

                htmlPageText1 = htmlPageText1.replace("<!-- {{ CEX_loss-value }} -->", str(sDeltaPercentCEX))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ DEX_loss-value }} -->", str(sDeltaPercentDEX))

                delta_prices = abs(Round(sRealExchangeCEX - sRealExchangeDEX, 2))
                delta_percents = Round(sDeltaPercentCEX - sDeltaPercentDEX, 2)

                htmlPageText1 = htmlPageText1.replace("<!-- {{ delta_prices }} -->", str(delta_prices))
                htmlPageText1 = htmlPageText1.replace("<!-- {{ delta_percents }} -->", str(delta_percents))

        else:
            htmlPageText1 = htmlPageText1.replace("\{\{ result_display \}\}", "none")

        
        self.wfile.write(bytes(htmlPageText1, "utf-8"))

        



if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")