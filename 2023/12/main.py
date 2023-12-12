from utils import *
from functools import cache

def main(input: str):
    lines = input.split("\n")
    lines = [line.split() for line in lines]
    lines = [[line[0], tuple(int(x) for x in line[1].split(","))] for line in lines]

    @cache
    def num_valid_solutions(txt: str, order: tuple):
        print(txt, order)
        if len(order) == 0:
            print("true",int("#" not in txt))
            return int("#" not in txt)

        if len(txt) < sum(order):
            print("false")
            return 0

        num_possible = 0
        if txt[0] == ".":
            txt = txt.lstrip(".")
            num_possible += num_valid_solutions(txt, order)
        else:
            next_p = txt.find(".")
            if (next_p >= order[0] and next_p != -1) or ("." not in txt and len(txt) >= order[0]):
                if len(txt) == order[0] or (txt[order[0]] in ".?"):
                    num_possible += num_valid_solutions(txt[order[0] + 1:], order[1:])
            if txt[0] in ".?":
                num_possible += num_valid_solutions(txt[1:], order)
        return num_possible

    possible = 0
    for line in lines:
        p = num_valid_solutions(line[0], line[1])
        print(p)
        print("----" * 10)
        possible += p
    return possible


if __name__ == '__main__':
    example_target = 21
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
