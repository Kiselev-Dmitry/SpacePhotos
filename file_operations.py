import os


def save_file(response, dir, topic, i, ext):
    if not os.path.exists(dir):
        os.makedirs(dir)
    print(i) # отладочный код
    filename = "{}/{}_{}{}".format(dir, topic, str(i), ext)
    with open(filename, "wb") as file:
        file.write(response.content)
