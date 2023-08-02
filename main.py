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

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
                    This script posts one photo to Telegram Channel.
                    User must indicate file in command line like this:
                    'python main.py -file spacex_4.jpeg'.
                    File must be loaded in directory, determined by DIR_WITH_PHOTOS in .env.
                    If no file selected script posts random file from the same directory.""")
    parser.add_argument('-file',
                        help="input file name for posting in TG-channel (default-random file)")
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




