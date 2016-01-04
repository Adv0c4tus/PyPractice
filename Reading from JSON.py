import urllib.request
import json

summ = 0
counter = 0

data = urllib.request.urlopen("http://python-data.dr-chuck.net/comments_203174.json").read()
js = json.loads(data.decode())
lenth = len(js['comments'])

while counter <lenth:
    summ += int(js['comments'][counter]['count'])
    counter += 1

print(summ)