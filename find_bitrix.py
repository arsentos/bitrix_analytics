from typing import List

import requests
from bs4 import BeautifulSoup


def find_bitrix(urls: List[str]):
    bitrix_list = ["bitrix", "bitrix24", "битрикс", "битрикс24", "1с-битрикс"]
    answer = {}
    headers = {
        'User-Agent': (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
            'Safari/537.36 OPR/97.0.0.0'),
        'Accept':
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
            'application/signed-exchange;v=b3;q=0.7',
        'Accept-Language':
            'ru-ru,ru;q=0.8,en-us;q=0.5,en;q=0.3',
        'Accept-Encoding':
            'gzip, deflate, br',
        'Connection':
            'keep-alive',
        'DNT':
            '1'
    }

    for url in urls:
        res = requests.get(url, headers=headers)
        html_lower = res.text.lower()
        for bitrix in bitrix_list:
            search_res = html_lower.find(bitrix)
            if search_res != -1:
                answer[url] = True
                break
            answer[url] = False
    return answer


result = find_bitrix(["https://it-solution.ru", "http://1-bit27.ru"])
print(result)