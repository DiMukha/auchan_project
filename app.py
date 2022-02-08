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
            try:
                session = requests.Session()
                response = requests.head(url[0], allow_redirects=True, timeout=10)
                print(response.url)
                print(url)
                print(response.url == url[0])
            except requests.exceptions.RequestException as ex:
                print(ex)
            continue


