from utils import *
from collections import defaultdict
#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    possible = input.splitlines()[0].split(", ")
    todo = input.splitlines()[2:]
    res = 0
    for t in todo:
        org_t = t
        next_t = []
        t = [t]
        while True:
            next_t = set()
            found = False
            print(t)
            for x in t:
                for p in possible:
                    if x == p:
                        res += 1
                        found = True
                        break
                    if x.startswith(p):
                        next_t.add(x[len(p):])
                if found:
                    break
            if found:
                break
            if not next_t:
                break
            t = next_t.copy()
    return res



def main(input: str):
    possible = input.splitlines()[0].split(", ")
    todo = input.splitlines()[2:]
    res = 0
    for t in todo:
        org_t = t
        next_t = []
        visited = set()
        t = {t : 1}
        print(res)
        while True:
            next_t = defaultdict(int)

            for x,i in t.items():
                for p in possible:
                    if x == p:
                        res += i
                    elif x.startswith(p):
                        next_t[x[len(p):]] += i

            if not next_t:
                break
            t = next_t.copy()
    return res



if __name__ == '__main__':
    example_target = 16
    with open("example.txt", "r") as f:
        example_output = main(f.read())

    if example_target is not None:
        if example_output == example_target:
            print(f"Example Output basst: {example_output}")
        else:
            print(f"example output basst nicht: {example_output} ;Target: {example_target}")
            exit()
    else:
        print(f"Example Output: {example_output}")

    with open("input.txt", "r") as f:
        input_output = main(f.read())

    print(f"Output: {input_output}")
