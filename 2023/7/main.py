from utils import recursive_split, all_different

ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
rev_order = list(reversed(ORDER))
def five_of_kind(inp):
    if len(set(inp)) == 1:
        return True
    return False


def four_of_kin(inp):
    if len(set(inp)) == 2:
        if inp.count(inp[0]) == 1 or inp.count(inp[0]) == 4:
            return True
    return False


def full_house(inp):
    if len(set(inp)) == 2:
        if inp.count(inp[0]) == 2 or inp.count(inp[0]) == 3:
            return True
    return False


def three_of_kin(inp):
    chars = set(inp)
    if len(chars) == 3:
        for c in chars:
            if inp.count(c) == 3:
                return True
    return False


def two_pair(inp):
    chars = set(inp)
    if len(chars) == 3:
        counts = []
        for c in chars:
            counts.append(inp.count(c))
        if 2 in counts and 1 in counts:
            return True
    return False


def one_pair(inp):
    if len(set(inp)) == 4:
        return True
    return False


def tr(inp):
    return True

def sort(lst: list, i):
    if len(lst) <= 1:
        return lst
    else:
        ret = [[] for _ in range(len(ORDER))]
        for l in lst:
            ret[rev_order.index(l[0][i])].append(l)
        if i < 5:
            ret = [sort(x, i+1) for x in ret]
        r = []
        for x in ret:
            r += x
        return r

def main(input: str):
    inp = recursive_split(input, "\n", " ")
    inp = [[x[0][0], int(x[1][0])] for x in inp]
    order = [[] for _ in range(7)]
    funcs = [five_of_kind, four_of_kin, full_house, three_of_kin, two_pair, one_pair, tr]
    for input in inp:
        for i, f in enumerate(funcs):
            if f(input[0]):
                order[i].append(input)
                break
    for i in range(7):
        order[i] = sort(order[i], 0)

    out = 0
    multiplier = 1
    print(order)
    for i in range(6,-1,-1):
        for j in range(len(order[i])):
            out += order[i][j][1] * multiplier
            print(order[i][j], multiplier)
            multiplier += 1

    return out




if __name__ == '__main__':
    example_target = 6440
    with open("example.txt", "r") as f:
        example_output = main(f.read())

    if example_target is not None:
        if example_output == example_target:
            print(f"Example Output basst: {example_output}")
        else:
            print(f"example output basst nicht: {example_output} ;Target: {example_target}")
    else:
        print(f"Example Output: {example_output}")

    with open("input.txt", "r") as f:
        input_output = main(f.read())

    print(f"Output: {input_output}")
