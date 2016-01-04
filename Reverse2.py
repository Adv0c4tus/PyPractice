TestList = 'abc'
def reverse(string):
    if isinstance(string, str):
        counter = 0
        return_str = str()
        length_of_str = len (string)
        while counter < (length_of_str):
            buffer = string[length_of_str-1-counter]
            return_str += buffer
            counter +=1
        return return_str
        #return string[::1-]
    #''.join()
    else:
        print ("Given argument is non a string")
result = reverse(TestList)
print (result)
assert reverse('abc') == 'cba'


