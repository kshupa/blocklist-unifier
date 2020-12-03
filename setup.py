from bs4 import BeautifulSoup
import html5lib
import requests


URL = "https://mirror1.malwaredomains.com/files/justdomains"
r = requests.get(URL)
block_list = BeautifulSoup(r.content, 'html5lib') 

block_list_name = 'Ultimate_block_list.txt'
with open(block_list_name, 'w') as f:
    f.write(block_list.prettify())