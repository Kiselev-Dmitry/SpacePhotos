import requests
import os
import argparse
from dotenv import load_dotenv

from file_operations import save_file


def fetch_spacex_last_launch(photo_dir, launch_id):
    spacex_url = "https://api.spacexdata.com/v5/launches/{}".format(launch_id)
    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]
    for index, image in enumerate(images):
        response = requests.get(image)
        response.raise_for_status()
        topic = "spacex"
        ext = ".jpeg"
        save_file(response, photo_dir, topic, index, ext)


if __name__ == "__main__":
    load_dotenv()
    photo_dir = os.environ["DIR_WITH_PHOTOS"]
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="""
                    This script downloads photos of specified SPACEX launch.
                    User must indicate launch id in command line like this:
                    'python fetch_spacex_images.py -launch_id 5eb87d47ffd86e000604b38a'.
                    If no launch indicated script downloads latest launch.
                    Files will be downloaded in directory, determined by DIR_WITH_PHOTOS in .env.""")
    parser.add_argument('-launch_id', default='latest',
                        help="Input launch_id after '-launch_id' (default - latest launch)")
    args = parser.parse_args()
    launch_id = args.launch_id
    fetch_spacex_last_launch(photo_dir, launch_id)
