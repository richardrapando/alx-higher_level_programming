#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints first x elements of a list and only integers
    Args:
        my_list(list): list to print elements
        x (int): number of elements of my_list to print

    Returns:
        number of printed integers 
    """
    man = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            man += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (man)
