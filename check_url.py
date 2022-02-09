import requests


class CheckURL:
    """
    Класс хранит результаты обработки URLs, использует requests (доступность, сокращение)
    Проверяет является ли URL сокращённым

    АТРИБУТЫ:
    --------
    timeout           : int - ожидание отклика URL в секундах, по умолчанию 10
    urls_status_codes : словарь {исходный URL: статус код}
    urls_unshorted    : словарь {исходный URL: полный URL}
    urls_error_check  : словарь {исходный URL: ошибка}
    urls_count        : подсчёт колличества URL

    МЕТОДЫ:
    ------
    availability      : проверка доступности, запись результата в urls_status_codes,
                        в случае ошибки запись в urls_error_check
    unshort           : запись в urls_unshorted
    """

    def __init__(self, timeout=10):
        self.timeout = timeout
        self.urls_status_codes = dict()
        self.urls_unshorted = dict()
        self.urls_error_check = dict()
        self.urls_count = 0

    def availability(self, url):
        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            self.urls_status_codes[url] = response.status_code
            self.urls_count += 1
            return response
        except requests.exceptions.RequestException as ex:
            self.urls_error_check[url] = ex

    def unshort(self, response, url):
        if response and url:
            self.urls_unshorted[url] = response.url
