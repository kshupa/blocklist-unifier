from bs4 import BeautifulSoup
import html5lib
import requests

def url_to_list(url):
    """Creates new txt file from given url."""

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html5lib')
    blocklist = soup.body.text

    with open('Ultimate_blocklist.txt', 'w') as file:
        file.write(blocklist)


def read_url_list(url_list):
    """Reads urls from thr source url_list."""
    with open('Source_list.txt', r) as file:
        file.read()


if __name__ == '__main__':
    url_to_list('https://mirror1.malwaredomains.com/files/justdomains')