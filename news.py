import requests
import os

NEWS_API_KEY = os.environ["NEW_API_KEY"]

class NewsManager():
    def __init__(self, company_name = "Tesla Inc") -> None: 
        self.company_name = company_name
    
    def get_news (self) -> list:
        params = {
            "q": self.company_name,
            "from":"2022-05-10",
            "sortBy":"popularity",
            "apiKey":NEWS_API_KEY, 
            "pageSize": 3
        }
        news_url = "https://newsapi.org/v2/everything"
        news_res = requests.get(url=news_url, params=params)
        news_res.raise_for_status()
        news_data = news_res.json()
        return news_data["articles"]