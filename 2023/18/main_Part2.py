from utils import *
import numpy as np

DIRECTIONS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0)
}
def main(input: str):
    input = [x.split()[-1][2:-1] for x in input.split("\n") if x != ""]
    points = [(0,0)]
    boundary = 0
    for x in input:
        distance = int("0x" + x[:-1], 0)
        dir_code = ("R","D","L","U")
        direction = dir_code[int(x[-1])]
        points.append((points[-1][0] + DIRECTIONS[direction][0] * distance, points[-1][1] + DIRECTIONS[direction][1] * distance))
        boundary += distance

    print(points)

    left = sum(points[i-1][0] * points[i][1] for i in range(len(points)))
    right = sum(points[i-1][1] * points[i][0] for i in range(len(points)))
    return 0.5 * abs(left - right) + boundary // 2 + 1



if __name__ == '__main__':
    example_target = 952408144115
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
