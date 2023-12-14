from utils import *


def main(input: str):
    input = [list(x) for x in input.split("\n")]
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

    load = 0
    for i in range(len(input)):
        load += sum([len(input) - i for x in input[i] if x == "O"])
    return load


if __name__ == '__main__':
    example_target = None
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
