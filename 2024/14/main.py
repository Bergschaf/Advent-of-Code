import time

from utils import *
import re
#parse_2D_grid_to_Defaultlist

#parse_numbers

def main(input: str):
    width = 101 # TODO change
    height = 103
    robots = [[int(y) for y in re.findall(r"(-?\d+)", x)] for x in input.splitlines()]
    positions = [x[:2] for x in robots]
    velocities = [x[2:] for x in robots]

    def move(position, velocity):
        new_pos = [position[0] + velocity[0], position[1] + velocity[1]]
        # wrap around
        if new_pos[0] < 0:
            new_pos[0] += width
        if new_pos[0] >= width:
            new_pos[0] -= width
        if new_pos[1] < 0:
            new_pos[1] += height
        if new_pos[1] >= height:
            new_pos[1] -= height
        return new_pos

    def visualize():
        s = " " * width + "\n"
        s *= height
        for p in positions:
            s = s[:p[0] + p[1] * (width + 1)] + "#" + s[p[0] + p[1] * (width + 1) + 1:]
        print(s)
    for i in range(10000):
       positions = [move(positions[i], velocities[i]) for i in range(len(positions))]
       visualize()
       print(i)




    q1, q2, q3, q4 = 0, 0, 0, 0
    for p in positions:
        if p[0] == width // 2 or p[1] == height // 2:
            continue
        if p[0] < width // 2 + 1:
            if p[1] < height // 2 :
                q1 += 1
            else:
                q4 += 1
        else:
            if p[1] < height // 2:
                q2 += 1
            else:
                q3 += 1
    return q1 * q2 * q3 * q4





if __name__ == '__main__':
    with open("input.txt", "r") as f:
        input_output = main(f.read())
    exit()
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
