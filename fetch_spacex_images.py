import requests
import argparse

from file_operations import save_file


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-launch_id', default='latest')
    return parser


def fetch_spacex_last_launch(dir):
    parser = create_parser()
    namespace = parser.parse_args()
    spacex_url = "https://api.spacexdata.com/v5/launches/{}".format(namespace.launch_id)
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]
    for i, image in enumerate(images):
        response = requests.get(image)
        response.raise_for_status()
        topic = "spacex"
        ext = ".jpeg"
        save_file(response, dir, topic, i, ext)


if __name__ == "__main__":
    dir = "images"
    fetch_spacex_last_launch(dir)
