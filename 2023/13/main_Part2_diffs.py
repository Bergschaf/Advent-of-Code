from utils import *


def main(input: str):
    input = [[list(x) for x in y.split("\n")] for y in input.split("\n\n")]

    def diff_list(x, l1):
        dist_to_edge = min(x, len(l1) - x)
        return sum(1 for i in range(dist_to_edge) if l1[x - i - 1] != l1[x + i])

    def diffs_vertical(i, grid):
        diff = 0
        for g in grid:
            diff += diff_list(i, g)
        return diff

    def diffs_horizontal(i, grid):
        diff = 0
        for ii in range(len(grid[0])):
            diff += diff_list(i, [x[ii] for x in grid])
        return diff

    vert = []
    hor = []
    for grid in input:
        z = 0
        for x in range(1, len(grid[0])):
            if diffs_vertical(x, grid) == 1:
                vert.append(x)
                z += 1
                break
        for y in range(1, len(grid)):
            if diffs_horizontal(y, grid) == 1:
                hor.append(y * 100)
                z += 1
                break
        if z == 2:
            print("none")
        if z == 0:
            print("au id gut")

    return sum(vert) + sum(hor)


if __name__ == '__main__':
    example_target = 400
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
