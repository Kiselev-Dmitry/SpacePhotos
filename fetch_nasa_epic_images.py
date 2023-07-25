import requests
import os
from dotenv import load_dotenv
import datetime


def fetch_nasa_epic(nasa_token, epic_count, dir):
    if not os.path.exists(dir):  # "Этот код вынести в общий файл
        os.makedirs(dir)
    payload = {"api_key": nasa_token}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", params=payload)
    response.raise_for_status()
    records = response.json()
    for i, record in enumerate(records):
        photo_name = record["image"]
        photo_date_str = record["date"]
        photo_date = datetime.datetime.strptime(photo_date_str, '%Y-%m-%d %H:%M:%S')
        photo_url = "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(
            photo_date.strftime('%Y/%m/%d'), photo_name)
        response = requests.get(photo_url, params=payload)
        response.raise_for_status()
        filename = '{}/nasa_epic_{}.png'.format(dir,str(i)) # "Этот код вынести в общий файл, ХОТЯ НЕ ФАКТ
        with open(filename, 'wb') as file:
             file.write(response.content)
        if i == int(epic_count): break  # Ограничиваем кол-во фотографий, т.к. очень долго грузятся


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    epic_count = os.environ["EPIC_COUNT"]
    dir = "images"
    fetch_nasa_epic(nasa_token, epic_count, dir)
