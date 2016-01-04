import string

def filter_bad_characters(data):
    """Return string with English-only characters from data"""
    result_str = str()
    buffer = []
    letter = str()
    etalon = string.ascii_letters
    for letter in data:
        if (letter in etalon):
            buffer.append(letter)
        else:
            pass
    result_str = "".join(buffer)
    return result_str

data = "4455887877asdffa8444444999848488484848511155asda115555asd1551"

print (filter_bad_characters(data))

assert filter_bad_characters('%#%@# W @ O #@# RD 2,,,') == 'WORD'

