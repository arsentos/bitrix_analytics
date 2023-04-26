import requests
from furl import furl
from bs4 import BeautifulSoup

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 '
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
number_of_sites = 0
number_of_requests = 0
url = "https://yapl.ru/ru.php?l=0&start=0"
a = furl(url)
step = 100
total = 0
with open("./p_t.txt", "a") as f:
    for i in range(26, 31):
        a.args["l"] = i
        a.args["start"] = 0
        html = requests.get(a.url, headers=headers)
        number_of_requests += 1
        soup = BeautifulSoup(html.content, features="lxml")
        form_with_num_of_pages = soup.find(id="form1").select("table tr td:last-child")
        number_of_pages = int(form_with_num_of_pages[0].text.split()[0])
        print(a.url, " Количество страниц ", number_of_pages)
        total += number_of_pages
        for j in range(0, number_of_pages*step, step):
            a.args["start"] = j
            inner_html = requests.get(a.url, headers=headers)
            number_of_requests += 1
            soup_1 = BeautifulSoup(inner_html.content, features="lxml")
            links = soup_1.select("#middleColumn div[align=center] > a")
            for link in links:
                f.write(f"{link.text}\n")
                number_of_sites += 1
            print(a.url, number_of_sites)
            print("Количество запросов:", number_of_requests)
    print(number_of_sites)
    print("всего:", total)