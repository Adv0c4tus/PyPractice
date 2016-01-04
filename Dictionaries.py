import string
import io
import sys
import re

counts = dict()
names = ['key1','key2','key3','key1']
for name in names:
    counts[name]= counts.get(name,0) + 1
print(counts)

stuff = dict()
print (stuff.get('candy',-1))

handle = open('C:/Users/Роман/Desktop/Py/mbox-short.txt', 'r')

words = list()
mails = dict()

for line in handle:
    if line.startswith('From '):
        words.append(line.split()[1])

for word in words:
    mails[word] = words.count(word)

MaxMail = None
MaxNum = None

for mail,numb in mails.items():
    if MaxNum is None or numb >= MaxNum:
        MaxNum = numb
        MaxMail = mail

print (MaxMail, MaxNum)

