#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_elts = 0

    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                printed_elts += 1
            except (ValueError, TypeError):
                continue
    except IndexError:
        pass

    print()
    return printed_elts
