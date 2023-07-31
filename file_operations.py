import os


def save_file(response, photo_dir, topic, index, ext):
    os.makedirs(photo_dir, exist_ok=True)
    filename = "{}/{}_{}{}".format(photo_dir, topic, str(index), ext)
    with open(filename, "wb") as file:
        file.write(response.content)
