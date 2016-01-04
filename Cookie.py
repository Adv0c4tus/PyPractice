import http.cookiejar, urllib.request
from bs4 import BeautifulSoup
import socket

connect_info = socket.getaddrinfo('www.pravda.com.ua', 80, proto=socket.IPPROTO_TCP)
print (connect_info)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(connect_info[0][4])

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open("http://www.pravda.com.ua/news/").read()

soup = BeautifulSoup(r,"html.parser")
print(soup.prettify())

sock.close()