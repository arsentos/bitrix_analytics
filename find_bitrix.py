from typing import List
import requests
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

def check_https_url(url):
    HTTPS_URL = f'https://{url}'
    try:
        HTTPS_URL = urlparse(HTTPS_URL)
        connection = HTTPSConnection(HTTPS_URL.netloc, timeout=2)
        connection.request('HEAD', HTTPS_URL.path)
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False

def check_http_url(url):
    HTTP_URL = f'http://{url}'
    try:
        HTTP_URL = urlparse(HTTP_URL)
        connection = HTTPConnection(HTTP_URL.netloc)
        connection.request('HEAD', HTTP_URL.path)
        if connection.getresponse():
            return True
        else:
            return False
    except:
        return False


def find_bitrix(urls: List[str]):
    bitrix_list = ["bitrix24", "битрикс24"]
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
        final_url = -1
        answer[url] = {}
        if check_https_url(url):
            final_url = f"https://{url}"
        else:
            final_url = f"http://{url}"
        try:
            res = requests.get(final_url, headers=headers)
            status = res.history[0].status_code if len(res.history) != 0 else res.status_code
            if status == 302 or status == 301:
                answer[url]["had_redirect"] = True
            else:
                answer[url]["had_redirect"] = False
            answer[url]["status"] = status
            html_lower = res.text.lower()
            for bitrix in bitrix_list:
                search_res = html_lower.find(bitrix)
                if search_res != -1:
                    answer[url]["found_bitrix"] = True
                    break
                answer[url]["found_bitrix"] = False
            answer[url]["error"] = None
            print(url, answer[url])
        except Exception as e:
            answer[url]["error"] = f"{e}"
            answer[url]["status"] = -1
            answer[url]["found_bitrix"] = False
            print(url, answer[url])
    return answer


lst = ["it-solution.ru"]
result = find_bitrix(lst)
print(result)