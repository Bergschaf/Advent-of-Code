from utils import *
import numpy as np

def main(input: str):
    input = [x.split() for x in input.split("\n") if x != ""]
    input = [(x[0],int(x[1])) for x in input]
    points = [(0,0,False)] # only works for inputs that start with r or l
    for direction, distance in input:
        if direction == "R":
            for i in range(distance):
                points.append((points[-1][0] + 1, points[-1][1], False))
            points[-1] = (points[-1][0], points[-1][1], True)
        elif direction == "L":
            for i in range(distance):
                points.append((points[-1][0] - 1, points[-1][1],False))
            points[-1] = (points[-1][0], points[-1][1], True)
        elif direction == "U":
            for i in range(distance):
                points.append((points[-1][0], points[-1][1] - 1, True))

        elif direction == "D":
            for i in range(distance):
                points.append((points[-1][0], points[-1][1] + 1, True))

    maxx = max([x[0] for x in points])
    maxy = max([x[1] for x in points])

    grid = np.zeros((maxx+1, maxy+1))
    for x,y,z in points:
        grid[x][y] = 1 if z else 2

    for i in grid:
        print(i)

    num_points = len(set(points))
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 0:
                num_grids = 0
                for i in range(y, len(grid[x])):
                    if grid[x][i] == 2:
                        num_grids += 1
                if num_grids % 2 != 0:
                    num_points += 1

    return num_points


if __name__ == '__main__':
    example_target = 63
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
