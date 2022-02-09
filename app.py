import sys
from urlextract import URLExtract
from loguru import logger

from config import Config
from load_file import load_pickle
from check_url import CheckURL


if __name__ == '__main__':

    logger.remove()
    logger.add(sys.stdout, format="[{time:HH:mm:ss}] <lvl>{message}</lvl>", level="INFO")
    logger.add(Config.LOG_PATH_FILENAME, rotation=Config.LOG_ROTATION, retention=Config.LOG_RETENTION)
    logger.info(f"Start program")

    data = load_pickle(Config.FILE_PATH)
    logger.info("File loaded")

    extractor = URLExtract()
    check_url = CheckURL()

    logger.info("Start parse and check")
    for row in data:
        url = extractor.find_urls(row)
        if url:
            response = check_url.availability(url[0])
            check_url.unshort(response, url[0])

            logger.info(f"URL {url} checked")

    print(check_url.urls_status_codes)
    print(check_url.urls_unshorted)
    print(check_url.urls_error_check)
    print(check_url.urls_count)

    logger.info("Finish program")
