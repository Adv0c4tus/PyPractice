import socket
import urllib.request
from bs4 import BeautifulSoup

#sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#sock.connect(('www.pravda.com.ua', 80))
#sock.send(b'GET http://www.pravda.com.ua/?attempt=1 HTTP/1.0\n\n')
#
#while True:
#    data = sock.recv(2048)
#    if ( len(data) < 1 ) :
#        break
#    print (data.decode())
#
#sock.close()

page = urllib.request.urlopen("http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html")
soup = BeautifulSoup(page,'lxml')
print (soup.prettify())
