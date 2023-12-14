from utils import *
from functools import cache


def main(input: str):
    input = [list(x) for x in input.split("\n")]
    move = True

    def roll_north(input):
        move = True
        while move:
            move = False
            for i in range(1, len(input)):
                for j in range(len(input[0])):
                    if input[i][j] == "O":
                        if input[i - 1][j] == ".":
                            input[i][j] = "."
                            input[i - 1][j] = "O"
                            move = True

    def roll_south(input):
        move = True
        while move:
            move = False
            for i in range(len(input) - 2, -1, -1):
                for j in range(len(input[0])):
                    if input[i][j] == "O":
                        if input[i + 1][j] == ".":
                            input[i][j] = "."
                            input[i + 1][j] = "O"
                            move = True

    def roll_east(input):
        move = True
        while move:
            move = False
            for i in range(len(input)):
                for j in range(len(input[0]) - 2, -1, -1):
                    if input[i][j] == "O":
                        if input[i][j + 1] == ".":
                            input[i][j] = "."
                            input[i][j + 1] = "O"
                            move = True

    def roll_west(input):
        move = True
        while move:
            move = False
            for i in range(len(input)):
                for j in range(1, len(input[0])):
                    if input[i][j] == "O":
                        if input[i][j - 1] == ".":
                            input[i][j] = "."
                            input[i][j - 1] = "O"
                            move = True

    prev = [[i.copy() for i in input]]
    for i in range(1,1000000000):
        roll_north(input)
        roll_west(input)
        roll_south(input)
        roll_east(input)
        print(i)

        if input in prev:
            loop_len = len(prev) - prev.index(input)
            left = (1000000000 - i) % loop_len
            input = prev[prev.index(input) + left]
            break

        prev.append([i.copy() for i in input])

    load = 0
    for i in range(len(input)):
        load += sum([len(input) - i for x in input[i] if x == "O"])
    return load


if __name__ == '__main__':
    example_target = 64
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
