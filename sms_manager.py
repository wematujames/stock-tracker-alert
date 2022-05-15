from twilio.rest import Client
import os

# Twillio auth
ACC_SID = os.environ["ACC_SID"]
AUTH_TOKEN =  os.environ["AUTH_TOKEN"]
MY_TWILLIO_NUM = os.environ["MY_TWILLIO_NUM"]
TWILIO_VERIFIED_NUM = os.environ["TWILIO_VERIFIED_NUM"]
   
class SMSManager():
    def __init__(self) -> None:
        pass

    def send_sms(articles: list, stock_down: bool, difference: int ) -> str: 
        '''Sends SMS based on if change in stock price >= 5%'''
        # Send an SMS for each article
        for i in range(len(articles)):
            news_item = articles[i]
            client = Client(ACC_SID, AUTH_TOKEN)
            message = client.messages \
                        .create(
                            body=f"""\n
                                TSLA: {"🔺" if not stock_down else "🔻"}{abs(difference)}%
                                Headline: {news_item["title"]}
                                Brief: {news_item["description"]}
                                """,
                            from_= MY_TWILLIO_NUM,
                            to= TWILIO_VERIFIED_NUM
                        )
        return message.sid