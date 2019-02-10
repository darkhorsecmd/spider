import os


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.mkdir(path)
