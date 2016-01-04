import string
import io
import sys
import re

handle = open('C:/Users/Роман/Desktop/Py/mbox-short.txt', 'r')
lst = list()
dct = dict()
for line in handle:
    line.rstrip()
    if line.startswith('From '):#фильтруем строки, берем все, что начинаются с "From "
        dct[line.split()[5].split(':')[0]] = dct.get(line.split()[5].split(':')[0],0)+1#разбиваем строку на элементы, берем пятый элемент - время, который разбиваем разделителем ":" и берем только часы. Считаем частоту
for time in sorted(dct):#идем по циклу отсортированного словаря (лист значений отсортированных ключей)
    print (time, dct[time])#выводим время и соответвующую ему частоту из словаря