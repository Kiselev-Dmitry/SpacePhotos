import requests
import pathlib
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import datetime
import telegram


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(tg_token)
    bot.send_document(chat_id="@trail_cosmos_photo", document=open('images/nasa_epic_4.png', 'rb'))


