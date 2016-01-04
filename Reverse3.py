global TestList
TestList = [1, 2, 3]
def reverse(items):
    if isinstance(items,list):
        length_of_list = len (items)
        reversedList = []
        counter = 0
        while counter < length_of_list:
            buffer = items[length_of_list-1-counter]
            reversedList.append(buffer)
            counter +=1
        counter = 0
        while counter < length_of_list:
            TestList[counter] = reversedList[counter]
            counter +=1
        del reversedList
    else:
        print ('Given argument is non a list')
reverse(TestList)
print (TestList)
assert TestList == [3, 2, 1]


