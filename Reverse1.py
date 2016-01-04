TestList = ['a', 'b', 'c']
def reverse(items):
    """
    :rtype : list
    """
    if isinstance(items, list):
        counter = 0
        length_of_list = len(items)
        reversed_list = []
        #while counter < (length_of_list):
        #    reversed_list.append(items[length_of_list-1-counter])
        #    counter +=1
        for index in reversed(range(len(items))):
            print (index)
            reversed_list.append(items[index])
        return reversed_list
        #return items[::-1]
    else:
        print ('Given argument is non a list')
result = reverse(TestList)
print (result)
assert reverse(['a', 'b', 'c']) == ['c', 'b', 'a']