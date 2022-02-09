import os


class Config:

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    FILE_PATH = os.path.join(ROOT_DIR, 'files/messages_to_parse.dat')
    LOG_PATH_FILENAME = os.path.join(ROOT_DIR, 'logs/file_{time}')
    LOG_ROTATION = "5 minute"
    LOG_RETENTION = "20 minute"
