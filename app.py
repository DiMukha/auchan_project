import sys
from urlextract import URLExtract
from loguru import logger

from config import Config
from load_file import load_pickle
from check_url import CheckURL


if __name__ == '__main__':
    logger.debug("Programm start")

    data = load_pickle(Config.FILE_PATH)
    extractor = URLExtract()
    check_url = CheckURL()

    for row in data:
        url = extractor.find_urls(row)
        if url:
            response = check_url.availability(url[0])
            check_url.unshort(response, url[0])


    print(check_url.urls_status_codes)
    print(check_url.urls_unshorted)
    print(check_url.urls_error_check)
    print(check_url.urls_count)


