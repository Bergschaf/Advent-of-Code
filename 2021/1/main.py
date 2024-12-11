from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main(input: str):
    res = 0
    input = [int(x) for x in input.splitlines()]
    for i in range(3, len(input)):
        if (input[i-3] + input[i-2] + input[i-1]) - (input[i-2] + input[i-1] + input[i]) < 0:
            res += 1


    return res


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
