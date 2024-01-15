#!/usr/bin/python3
"""Task 1 : My list """


class MyList(list):
    """class MyList that inherits from list
        Attributes:
            Public instance method: print_sorted """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort) """
        return print(sorted(self))
