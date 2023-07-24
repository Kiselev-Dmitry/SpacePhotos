import requests
import pathlib
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import datetime

def fetch_spacex_last_launch(dir):
    # Не сделал - ввод номера старта через agrparse - см. Counting clicks
    load_dotenv()
    spacex_id = os.environ["SPACEX_ID"]
    spacex_url = "https://api.spacexdata.com/v5/launches/{}".format(spacex_id)

    if not os.path.exists(dir):
        os.makedirs(dir)
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]
    for i, image in enumerate(images):
        response = requests.get(image)
        response.raise_for_status()
        filename = '{}/hubble{}.jpeg'.format(dir,str(i))
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    dir = "images"
    fetch_spacex_last_launch(dir)
