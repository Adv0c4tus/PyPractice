haystack = [1, 10, 50, 100, 500, 600, 800]

def find_in_sorted_list(needle, haystack):
    if haystack.count(needle) == 0:
        print("No matches")
    else:
        length_of_heystack = len(haystack)
        midl_element_num = (length_of_heystack // 2)
        if haystack[midl_element_num] == needle:
            return midl_element_num
        elif haystack[midl_element_num] > needle:
            counter = midl_element_num
            while (counter - 1) > 0:
                if haystack[counter - 1] == needle:
                    return int(counter - 1)

                else:
                    counter -= 1
        else:
            counter = midl_element_num
            while counter < length_of_heystack:
                if haystack[counter + 1] == needle:
                    return int(counter + 1)
                else:
                    counter += 1

print(find_in_sorted_list(50, haystack))

assert find_in_sorted_list(50, haystack) == 2
assert find_in_sorted_list(500, haystack) == 4
assert find_in_sorted_list(800, haystack) == 6
