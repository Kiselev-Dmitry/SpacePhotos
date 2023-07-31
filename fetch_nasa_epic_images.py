import requests
import os
from dotenv import load_dotenv
from datetime import datetime

from file_operations import save_file


def fetch_nasa_epic(nasa_token, epic_count, photo_dir):
    payload = {"api_key": nasa_token}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=payload)
    response.raise_for_status()
    records = response.json()
    for index, record in enumerate(records):
        photo_name = record["image"]
        photo_date_date = datetime.fromisoformat(record["date"]).date()
        photo_date_str = str(photo_date_date).replace("-", "/")
        photo_url = "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(
            photo_date_str, photo_name)
        response = requests.get(photo_url, params=payload)
        response.raise_for_status()
        topic = "nasa_epic"
        ext = ".png"
        save_file(response, photo_dir, topic, index, ext)
        if index == int(epic_count): break  # Ограничиваем кол-во фотографий, т.к. очень долго грузятся


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    epic_count = os.environ["EPIC_COUNT"]
    photo_dir = os.environ["DIR_WITH_PHOTOS"]
    fetch_nasa_epic(nasa_token, epic_count, photo_dir)
