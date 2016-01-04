import socket
import urllib.request
from bs4 import BeautifulSoup
import html5lib

summ = 0
page = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_203173.html")
soup = BeautifulSoup(page, 'html5lib')
tags = soup('span')


for tag in tags:
    summ = summ + int(tag.contents[0])

print ('The sum is %s' % summ)

tags = soup('a')
for tag in tags:
    print (tag.get('href', None))