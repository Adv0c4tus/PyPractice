from Reverse3 import reverse
TestList = 256
def sum_of_digits(n):
    if isinstance(n,int):
        counter = 0
        return_sum = int()
        digits_str = str(n)
        length_of_str = len (digits_str)
        while counter < (length_of_str):
            return_sum += int(digits_str[length_of_str-1-counter])
            counter +=1
        return return_sum
    else:
        print ("Given argument is non a integer")

assert sum_of_digits(256) == 13
print (sum_of_digits(256))
assert sum_of_digits(512) == 8
print (sum_of_digits(512))
assert sum_of_digits(111) == 3
print (sum_of_digits(111))


