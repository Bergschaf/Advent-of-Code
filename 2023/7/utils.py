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
