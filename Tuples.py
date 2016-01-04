import string
import io
import sys
import re


fhand = open('C:/Users/Роман/Desktop/Py/romeo.txt', 'r')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
print(sorted(counts))
lst = list()
for key,val in counts.items():
    lst.append((val,key))
lst.sort(reverse=True)
print(lst)


