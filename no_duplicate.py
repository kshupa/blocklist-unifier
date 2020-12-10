from bs4 import BeautifulSoup
import html5lib
import requests
import url_to_list

def remove_duplicates():
    """Removes duplicate blocking urls."""

    with open('Ultimate_blocklist.txt', 'r') as source_file:
        content_set = set(source_file.readlines())
        with open('Ultimate_blocklist.txt', 'w') as final_file:
            for line in content_set:
                final_file.writelines(line)


if __name__ == '__main__':
    remove_duplicates()
    

    