import os


def check_path(path, is_make=True):
    if not os.path.exists(path=path):
        if is_make:
            os.mkdir(path=path)
            raise Exception("Path %s is new created" % path)
        else:
            raise FileNotFoundError("Path %s is not Found" % path)