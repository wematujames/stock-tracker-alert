import requests
import datetime as dt
import os

AV_API_KEY = os.environ["AV_API_KEY"]

class StockManager ():
    def __init__(self, company = "TSLA"):
        self.company = company
        self.stock_price_change =None
        self.getStockPrices()
    
    def getStockPrices(self, prev_day = 1, prev_prev_day = 2) -> None:
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.company}&apikey={AV_API_KEY}"
        print(url)
        res = requests.get(url=url)
        res.raise_for_status()
        data = res.json()
        
        
        # Get date for yesterday and day before
        yesty_date = str(dt.datetime.now() - dt.timedelta(days=prev_day))[:10]
        yesty_yesty_date = str(dt.datetime.now() - dt.timedelta(days=prev_prev_day))[:10]
        
        # Extract closing  values for yesterday and day before
        try:
            stock_yesterday = float(data["Time Series (Daily)"][yesty_date]["4. close"])
            stock_2days_ago = float(data["Time Series (Daily)"][yesty_yesty_date]["4. close"])
        except KeyError:
            print("Data for previous day(s) not available hence loading most recent data")
            self.getStockPrices(prev_day=prev_day + 1, prev_prev_day= prev_prev_day + 1)
        else:
            self.stock_price_change = round(((stock_2days_ago - stock_yesterday) / stock_2days_ago) * 100)
        
    def is_big_difference(self):
        '''Basically check if the difference between the stock price two ago and yesterday >= 5%'''

        if abs(self.stock_price_change) >= 0:
            return True
        return False
    
    def is_stock_down (self):
        if self.stock_price_change > 0:
            return False
        return True
    