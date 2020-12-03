from bs4 import BeautifulSoup
import html5lib
import requests

def url_to_list(url):
    # URL = "https://mirror1.malwaredomains.com/files/justdomains"
    r = requests.get(url)
    block_list = BeautifulSoup(r.content, 'html5lib') 

    with open('Ultimate_block_list.txt', 'w') as file:
        file.write(block_list.prettify())

if __name__ == '__main__':
    url_to_list(https://mirror1.malwaredomains.com/files/justdomains)