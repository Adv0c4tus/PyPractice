import collections
import string
import operator

def filter_noise(data):
    """Return string with noise(Non Lettter characters from data)"""
    noise = str()
    buffer = []
    letter = str()
    etalon = string.ascii_letters
    for letter in data:
        if not (letter in etalon):
            buffer.append(letter)
        else:
            pass
    noise = "".join(buffer)
    return noise

def char_distribution(data):
    """Return distribution of characters in data as dict"""
    c = collections.Counter(data).most_common()
    c_res = dict(c)
    return c_res


def most_common_char(data):
    buffer = char_distribution(data)
    result = max(buffer.keys(), key=(lambda k: buffer[k]))
    return result

def least_common_char(data):
    buffer = char_distribution(data)
    result = min(buffer.keys(), key=(lambda k: buffer[k]))
    return result


raw_data = "asdasdfggasdasd55559888asd88as8d8asd  ::'asd!!!!!!!!!! "
data = filter_noise(raw_data)
result_distr = char_distribution(data)
result_most_common = most_common_char(data)
result_least_common = least_common_char(data)

print(result_distr)
print(result_most_common)
print(result_least_common)

assert most_common_char('aabbbcccc') == 'c'
assert char_distribution('aabbbcccc') == {'a': 2, 'b': 3, 'c': 4}
assert least_common_char('aabbbcccc') == 'a'