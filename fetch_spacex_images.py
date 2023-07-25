import requests
import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-launch_id', default='latest') # ???
    return parser


def fetch_spacex_last_launch(dir):
    parser = create_parser()
    namespace = parser.parse_args()
    spacex_url = "https://api.spacexdata.com/v5/launches/{}".format(namespace.launch_id)

    if not os.path.exists(dir):
        os.makedirs(dir)

    response = requests.get(spacex_url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]
#    print(images) # отладочный код
    for i, image in enumerate(images):
        response = requests.get(image)
#        print(image)  # отладочный код
        response.raise_for_status()
        filename = '{}/hubble{}.jpeg'.format(dir,str(i))
        with open(filename, 'wb') as file:
            file.write(response.content)


if __name__ == "__main__":
    dir = "images"
    fetch_spacex_last_launch(dir)
