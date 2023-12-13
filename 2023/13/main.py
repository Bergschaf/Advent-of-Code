from utils import *


def main(input: str):
    input = [[list(x) for x in y.split("\n")] for y in input.split("\n\n")]

    def is_horizontal_line(x, grid):
        dist_to_edge = min(x, len(grid) - x)
        for i in range(dist_to_edge):
            if grid[x - i - 1] != grid[x + i]:
                return False
        return True

    def is_vertical_line(y, grid):
        dist_to_edge = min(y, len(grid[0]) - y)
        for i in range(dist_to_edge):
            if [x[y + i] for x in grid] != [x[y - i - 1] for x in grid]:
                return False
        return True

    vert = []
    hor = []
    for grid in input:
        for x in range(1, len(grid)):
            if is_horizontal_line(x, grid):
                hor.append(x * 100)
                break
        for y in range(1, len(grid[0])):
            if is_vertical_line(y, grid):
                vert.append(y)
                break
        print("none")

    return sum(vert) + sum(hor)

#27326


if __name__ == '__main__':
    example_target = 405
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
