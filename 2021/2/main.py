from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    hor = 0
    ver = 0
    input = [(int( x.split()[1]), x.split()[0]) for x in input.splitlines()]
    print(input)
    for val, dir in input:
        if dir == "forward":
            ver += val
        elif dir == "up":
            hor += val
        elif dir == "down":
            hor -= val
    return hor * ver
def main(input: str):
    hor = 0
    ver = 0
    aim = 0
    input = [(int( x.split()[1]), x.split()[0]) for x in input.splitlines()]
    print(input)
    for val, dir in input:
        if dir == "forward":
            ver += val
            hor += aim * val
        elif dir == "up":
            aim -= val
        elif dir == "down":
            aim += val
    return hor * ver

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
