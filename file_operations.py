import os


def save_file(response, photo_dir, topic, i, ext):
    if not os.path.exists(photo_dir):
        os.makedirs(photo_dir)
    filename = "{}/{}_{}{}".format(photo_dir, topic, str(i), ext)
    with open(filename, "wb") as file:
        file.write(response.content)
