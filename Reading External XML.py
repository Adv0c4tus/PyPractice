import urllib.request
import xml.etree.ElementTree as ET

summ = 0
data = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_203170.xml").read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')

for count in counts:
    summ += int(count.text)

print(summ)

