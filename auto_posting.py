import os
from dotenv import load_dotenv
import telegram
import random
import time


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(tg_token)
    chat_id = os.environ["CHAT_ID"]
    photo_dir = os.environ["DIR_WITH_PHOTOS"]
    images = os.listdir(path=photo_dir)
    post_interval = os.environ["POST_INTERVAL"]

    while True:
        for image in images:
            bot.send_document(chat_id=chat_id, document=open('{}/{}'.format(photo_dir, image), 'rb'))
            time.sleep(int(post_interval))
        random.shuffle(images)

