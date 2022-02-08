import os


class Config:

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(ROOT_DIR, 'files\messages_to_parse.dat')
