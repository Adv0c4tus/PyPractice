import requests
import http.cookiejar, urllib.request
from bs4 import BeautifulSoup

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]
r = opener.open("http://www.pravda.com.ua/news/").read()

soup = BeautifulSoup(r,"html.parser")
print (soup.prettify())