import requests
from urlextract import URLExtract

from config import Config
from load_file import load_pickle


if __name__ == '__main__':

    data = load_pickle(Config.FILE_PATH)


    extractor = URLExtract()
    for row in data:
        url = extractor.find_urls(row)
        if url:
            print(url)
            if len(url) > 1:
                print(f"LEN URL = {len(url)}")
            try:
                print(requests.head(url[0], timeout=10))
            except requests.exceptions.RequestException as ex:
                print(ex)
            continue


