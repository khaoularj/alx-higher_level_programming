#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for element in range(list_length):
        try:
            res = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            n_list.append(res)
    return (n_list)
