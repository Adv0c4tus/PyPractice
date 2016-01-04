import urllib.request
from bs4 import BeautifulSoup


position = 18
iterations = 7
counter = 1
start_link = "https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Patrikas.html"

page = urllib.request.urlopen(start_link)
soup = BeautifulSoup(page, 'lxml')
tags_init = soup('a')
link2go = str((tags_init[position-1].get('href', None)))

while counter < iterations:
    buffer_count = urllib.request.urlopen(link2go)
    soup_count = BeautifulSoup(buffer_count, 'lxml')
    tags_count = soup_count('a')
    link2go = str((tags_count[position-1].get('href', None)))
    counter += 1

print(link2go)
