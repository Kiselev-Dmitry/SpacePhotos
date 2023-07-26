import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

from file_operations import save_file


def fetch_nasa_apod(nasa_token, apod_count, dir):
    payload = {"api_key": nasa_token,
               "count": apod_count}
    response = requests.get("https://api.nasa.gov/planetary/apod", params=payload)
    response.raise_for_status()
    records = response.json()
    for i, record in enumerate(records):
        if record["media_type"] != "video":
            record_url = record["url"]
            response = requests.get(record_url)
            response.raise_for_status()
            topic = "nasa_apod"
            ext = get_ext(record_url)
            save_file(response, dir, topic, i, ext)


def get_ext(record_url):
    parsed_path = urlparse(record_url).path
    result = os.path.splitext(parsed_path)
    return result[1]


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    apod_count = os.environ["APOD_COUNT"]
    dir = "images"
    fetch_nasa_apod(nasa_token, apod_count, dir)
