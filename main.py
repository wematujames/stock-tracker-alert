from sms_manager import SMSManager
from news import NewsManager
from stock import StockManager


# Get stock  # Default company TSLA for both
stock_manager  = StockManager() 
news_manager = NewsManager() 

# Get news if difference is big
if stock_manager.is_big_difference():
    news_articles = news_manager.get_news()
    SMSManager.send_sms(news_articles, stock_manager.is_stock_down, stock_manager.stock_price_change)