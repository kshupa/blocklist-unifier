from bs4 import BeautifulSoup
import html5lib
import requests
import sys


def url_to_list():
    """Creates new txt file from given url."""

    with open('Ultimate_blocklist.txt', 'a') as block_file:
        new_url = sys.argv[1]
        print(new_url)
        res = requests.get(new_url)
        soup = BeautifulSoup(res.content, 'html5lib')
        blocklist = soup.body.text
        block_file.writelines(blocklist)


if __name__ == '__main__':
    url_to_list()