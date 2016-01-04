import string
import io
import sys
import re

data = open('C:/Users/Роман/Desktop/Py/regex_sum_203168.txt', 'r')
sum = 0
for lines in data:
   buffer = re.findall('[0-9]+', lines)
   for num in buffer:
       sum += int(num)
print (sum)

fh = open('C:/Users/Роман/Desktop/Py/romeo.txt', 'r')
lst = list()
for line in fh:
    line.rstrip()
    for word in line.split():
        if word in lst: continue
        else: lst.append(word)
print(lst)

fg = open('C:/Users/Роман/Desktop/Py/mbox-short.txt', 'r')
counter = 0
for line in fg:
    line.rstrip()
    if line.startswith('From '):
        print(line.split()[1])
        counter += 1
print (counter)





