#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elements of a given list.

    Args:
        my_list (list): list to print elements from.
        x (int): number of elements of my_list to get printed.

    Returns:
        printed number of elements.
    """

    man = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            man += 1
        except IndexError:
            break

    print("")
    return (man)
