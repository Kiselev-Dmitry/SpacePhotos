import requests
import pathlib
from urllib.parse import urlparse
import os
from dotenv import load_dotenv
import datetime


# def fetch_spacex_last_launch(spacex_url, dir):
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     response = requests.get(spacex_url)
#     response.raise_for_status()
#     images = response.json()["links"]["flickr"]["original"]
#     for i, image in enumerate(images):
#         response = requests.get(image)
#         response.raise_for_status()
#         filename = '{}/hubble{}.jpeg'.format(dir,str(i))
#         with open(filename, 'wb') as file:
#             file.write(response.content)


# def get_nasa_apod(nasa_apod_url, nasa_token, dir):
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     payload = {"api_key": nasa_token,
#                "count": "5"}
#     response = requests.get(nasa_apod_url, params=payload)
#     response.raise_for_status()
#     records = response.json()
# #    print(records) # Отладочный код
#     for i, record in enumerate(records):
#         if record["media_type"] != "video":
#             record_url = record["url"]
#             response = requests.get(record_url)
#             response.raise_for_status()
#             filename = '{}/nasa_apod_{}{}'.format(dir,str(i), get_ext(record_url))
#             with open(filename, 'wb') as file:
#                 file.write(response.content)


# def get_nasa_epic(nasa_epic_url, nasa_token, dir):
#     if not os.path.exists(dir):
#         os.makedirs(dir)
#     payload = {"api_key": nasa_token}
#     response = requests.get(nasa_epic_url, params=payload)
#     response.raise_for_status()
#     records = response.json()
#     print(response.json()[0]["image"]) # Отладочный код
#     for i, record in enumerate(records):
#         photo_name = record["image"]
#         photo_date_str = record["date"]
#         photo_date = datetime.datetime.strptime(photo_date_str, '%Y-%m-%d %H:%M:%S')
#         photo_url = "https://api.nasa.gov/EPIC/archive/natural/{}/png/{}.png".format(
#             photo_date.strftime('%Y/%m/%d'), photo_name)
#         print(i) # Отладочный код
# #        print(photo_url) # Отладочный код
#         response = requests.get(photo_url, params=payload)
#         response.raise_for_status()
#         filename = '{}/nasa_epic_{}.png'.format(dir,str(i))
#         with open(filename, 'wb') as file:
#              file.write(response.content)
#         if i == 6: break # Ограничиваем кол-во фотографий, т.к. очень долго грузятся

# def get_ext(record_url):
#     parsed_path = urlparse(record_url).path
#     result = os.path.splitext(parsed_path)
#     return result[1]


if __name__ == "__main__":
    load_dotenv()
#    spacex_id = os.environ["SPACEX_ID"]
    nasa_token = os.environ["NASA_TOKEN"]
    dir = "images"

#    nasa_apod_url  = "https://api.nasa.gov/planetary/apod"
#    get_nasa_apod(nasa_apod_url, nasa_token, dir)

    nasa_epic_url  = "https://api.nasa.gov/EPIC/api/natural/images"
    get_nasa_epic(nasa_epic_url, nasa_token, dir)
