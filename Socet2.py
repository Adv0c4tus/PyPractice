import re
import socket
import urllib.request
import requests
from bs4 import BeautifulSoup


connect_info = socket.getaddrinfo("www.pravda.com.ua", 80, proto=socket.IPPROTO_TCP)
print (connect_info)
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.connect(connect_info[0][4])

#r = requests.get("https://www.pravda.com.ua/news/",cookies=cookies)
#soup = BeautifulSoup(r.content,"html.parser")
page = urllib.request.urlopen("http://www.pravda.com.ua/?attempt=1")
soup = BeautifulSoup(page.read(),"html.parser")
print(soup.prettify())

#print (soup.prettify())

#while True:
#    data = sock.recv(1024)
#    if ( len(data) < 1 ) :
#        break
#    soup = BeautifulSoup(sock,"lxml")
#    print (soup.prettify())

sock.close()