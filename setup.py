from bs4 import BeautifulSoup
import html5lib
import requests

# def read_url_list():
#     """Reads urls from thr source url_list."""
#     with open('Source_list.txt', 'r') as file:
#         for url in file:
#             return url


def url_to_list():
    """Creates new txt file from given url."""

    with open('Source_list.txt', 'r') as source_file:
        with open('Ultimate_blocklist.txt', 'w') as block_file:
            for line in source_file:
                print(line)
                res = requests.get(line)
                soup = BeautifulSoup(res.content, 'html5lib')
                blocklist = soup.body.text
                block_file.writelines(blocklist)


if __name__ == '__main__':
    url_to_list()
    

    