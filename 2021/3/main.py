from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main(input: str):
    gamma = []
    epsi = []
    input = [list(x) for x in input.splitlines()]
    x = [[] for _ in range(len(input[0]))]
    for i in input:
        for ii, y in enumerate(i):
            x[ii].append(y)
    input = x



    for i in input:
        one_count = i.count("1")
        zero_count = i.count("0")
        most_common = "1" if one_count > zero_count else "0"
        gamma.append(most_common)
        epsi.append("0" if most_common == "1" else "1")
    gamma, epsi = "".join(gamma), "".join(epsi)

    return int(gamma, 2) * int(epsi, 2)

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
