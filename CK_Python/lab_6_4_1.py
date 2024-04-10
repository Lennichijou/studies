import concurrent.futures
import urllib.request

urls = [
    "https://miet.ru/news/158598",
    "https://miet.ru/structure/s/2775",
    "https://google.com",
    "https://vk.com/login",
    "https://dzen.ru",
    "https://stepik.org",
    "https://example.com/",
    "https://www.opennet.ru/",
    "https://example.net/",
    "https://example.org",
]


def get_site_data(url):
    data = urllib.request.urlopen(url)
    file = open(f"{url.replace('https://', '').replace('/', '')}.txt", "w")
    file.write(data.read().decode('cp1251'))
    file.close()


with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(get_site_data, urls)
