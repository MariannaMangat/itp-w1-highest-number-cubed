"""This is the entry point of the program."""


def highest_number_cubed(limit):
    num = 1
    while limit > num:
        num = num **3
    return limit
        
