from utils import *
import numpy as np
from functools import cache
import sys

sys.setrecursionlimit(1000000)


def main(input: str):
    input = [x.split() for x in input.split("\n") if x != ""]
    input = [(x[0], int(x[1])) for x in input]
    points = [(0, 0, False)]  # only works for inputs that start with r or l
    for direction, distance in input:
        if direction == "R":
            for i in range(distance):
                points.append((points[-1][0] + 1, points[-1][1], False))
        elif direction == "L":
            for i in range(distance):
                points.append((points[-1][0] - 1, points[-1][1], False))
        elif direction == "U":
            for i in range(distance):
                points.append((points[-1][0], points[-1][1] - 1, True))
            points[-1] = (points[-1][0], points[-1][1], False)

        elif direction == "D":
            for i in range(distance):
                points.append((points[-1][0], points[-1][1] + 1, True))
            points[-1] = (points[-1][0], points[-1][1], False)

    maxx = max([x[0] for x in points])
    minx = min([x[0] for x in points])
    maxy = max([x[1] for x in points])
    miny = min([x[1] for x in points])
    minx = abs(minx)
    miny = abs(miny)
    grid = np.zeros((maxx + 1 + minx, maxy + 1 + miny))
    for x, y, z in points:
        grid[x + minx][y + miny] = 1

    # floodfill
    in_grid = []

    searched = []

    def get_neightbours(x, y):
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    outside_points = []
    inside_points = []
    num_in_grid = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 1:
                num_in_grid += 1
            else:
                if (x, y) in inside_points:
                    num_in_grid += 1
                    continue
                elif (x, y) in outside_points:
                    continue
                stack = [(x, y)]
                out = None
                searched = [(x, y)]
                while len(stack) > 0:
                    x, y = stack.pop()
                    searched.append((x, y))
                    if (x, y) in outside_points:
                        out = True
                        break
                    elif (x, y) in inside_points:
                        out = False
                        break
                    if grid[x][y] == 1:
                        continue
                    for x1, y1 in get_neightbours(x, y):
                        if x1 <= 0 or y1 <= 0 or x1 >= len(grid)-1 or y1 >= len(grid[x1])-1:
                            out = True
                            break
                        else:
                            if (x1, y1) not in searched:
                                stack.append((x1, y1))
                else:
                    out = False
                if out:
                    outside_points.extend(searched)
                else:
                    inside_points.extend(searched)
                    num_in_grid += 1

    return num_in_grid


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
