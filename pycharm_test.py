from threading import Thread

import requests


def download(url):
    response = requests.get(url)
    if response.status_code == 200:
        print('Success -> {:<75} | Length -> {}' .format(response.url, len(response.content)))
    else:
        print("Failure -> {:>75}" .format(response.url))


if __name__ == '__main__':
    urls = ('http://www.google.com', 'http://www.hpe.com', 'http://www.microsoft.com')

    for u in urls:
        Thread(target=download, args=(u,)).start()

