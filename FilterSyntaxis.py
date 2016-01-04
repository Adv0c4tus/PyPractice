import string
import operator
a = list(map(chr,range(32,127)))
b = list(filter(lambda x: x > 100, range(32,127)))

people = [{'name':"Vasia",'age':50},{'name':"Petia","lastname":"Petrov",'age':28},{'name':'Olga','age':25}]

for person in people:
    if person['age'] > 26:
        print(person['name'])
filtered = [person for person in people if person['age'] > 26]

names = [x['name'] for x in people]

names_1 = list(map(lambda person: person['name'], people))

old_ppl = list(filter(lambda person: person['age'] > 26, people))

for index, person in enumerate(people):
    print(index, person['name'])

#skleivanie ryadov
seq1 = range(1,6)
seq2 = range(6,11)

for a, b in zip(seq1,seq2):
    print (a,b)
#sortirovka
lst = [1,5,-10,20,30,-100,-42,3,2,7,6]

def invert(a):
    return -a

for item in sorted(lst, key=invert):
    print(item)
