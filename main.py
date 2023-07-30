import argparse
import os
from dotenv import load_dotenv
import telegram
import random


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-file')
    return parser


if __name__ == "__main__":
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(tg_token)
    photo_dir = os.environ["DIR_WITH_PHOTOS"]
    chat_id = os.environ["CHAT_ID"]
    images = os.listdir(path=photo_dir)

    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.file: image = namespace.file
    else: image = random.choice(images)
    bot.send_document(chat_id=chat_id, document=open('{}/{}'.format(photo_dir, image), 'rb'))


