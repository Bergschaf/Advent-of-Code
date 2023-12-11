def all_different(lst: list):
    """
    Check if all elements in the list are different
    """
    return len(lst) == len(set(lst))


def recursive_split(string, *args):
    """
    Split a string recursively by multiple delimiters
    """
    if len(args) == 0:
        return [string]
    else:
        split = string.split(args[0])
        return [recursive_split(s, *args[1:]) for s in split]

def lower_alphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def upper_alphabet():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def last_int(string):
    """
    Get the last integer in a string, the last integer is separated by a space
    """
    return int(string.split()[-1])