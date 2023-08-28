#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for element in my_list[:x]:
        try:
            if count < x and type(element) is int:
                print("{:d}".format(element), end="")
                count += 1
        except IndexError:
            continue
    print()
    return count
