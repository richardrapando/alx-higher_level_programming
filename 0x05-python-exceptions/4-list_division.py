#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """divides en lement by element 2 lists
    Args:
        my_list_1 (list): first list
        my_list_2 (list): second list
        list_length (int): length integer, can be bigger than both

    Returns:
        a new list (length = list_length)
    """
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return (new_list)
