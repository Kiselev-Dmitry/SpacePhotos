import argparse
import os
from dotenv import load_dotenv
import telegram
import random


def main():
    load_dotenv()
    tg_token = os.environ["TG_TOKEN"]
    bot = telegram.Bot(tg_token)
    photo_dir = os.environ["DIR_WITH_PHOTOS"]
    chat_id = os.environ["TG_CHANNEL_ID"]
    images = os.listdir(path=photo_dir)

    parser = argparse.ArgumentParser()
    parser.add_argument('-file', help="input file name for posting in TG-channel (default - random file)")
    args = parser.parse_args()
    if args.file:
        image = args.file
    else:
        image = random.choice(images)
    filename = '{}/{}'.format(photo_dir, image)
    with open(filename, "rb") as file:
        bot.send_document(chat_id=chat_id, document=file)


if __name__ == "__main__":
    main()




