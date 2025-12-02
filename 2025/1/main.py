from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    dial = 50
    n = 0
    for line in input.splitlines():
        if line[0] == "R":
            dial += int(line[1:])
            n += dial // 100
        else:
            dial -= int(line[1:])

            n -= dial // 100
        dial %= 100

    return n

def main(input: str):
    dial = 50
    n = 0
    for line in input.splitlines():
        if line[0] == "R":
            for i in range(int(line[1:])):
                dial += 1
                dial %= 100

                if dial == 0:
                    n += 1

        else:
            for i in range(int(line[1:])):
                dial -= 1
                dial %= 100

                if dial == 0:
                    n += 1



    return n
# 6580


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
