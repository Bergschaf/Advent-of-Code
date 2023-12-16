from utils import *
import sys
sys. setrecursionlimit(100000)

def main(input: str):
    grid = parse_grid(input)
    direction = (1, 0)  # x, y
    position = (0, 0)
    energized = []

    def move_beam(direction, position):
        if (position, direction) in energized:
            return None

        energized.append((position, direction))
        position = (position[0] + direction[0], position[1] + direction[1])
        if position[0] >= len(grid[0]) or position[1] >= len(grid) or position[0] < 0 or position[1] < 0:
            return None

        if grid[position[1]][position[0]] == "/":
            if direction == (1, 0):
                direction = (0, -1)
            elif direction == (-1, 0):
                direction = (0, 1)
            elif direction == (0, 1):
                direction = (-1, 0)
            elif direction == (0, -1):
                direction = (1, 0)
        elif grid[position[1]][position[0]] == "\\":
            if direction == (1, 0):
                direction = (0, 1)
            elif direction == (-1, 0):
                direction = (0, -1)
            elif direction == (0, 1):
                direction = (1, 0)
            elif direction == (0, -1):
                direction = (-1, 0)
        elif grid[position[1]][position[0]] == "-":
            if direction == (0, 1) or direction == (0, -1):
                move_beam((1, 0), position)
                move_beam((-1, 0), position)
                return None
        elif grid[position[1]][position[0]] == "|":
            if direction == (1, 0) or direction == (-1, 0):
                move_beam((0, 1), position)
                move_beam((0, -1), position)
                return None
        move_beam(direction, position)

    if grid[position[1]][position[0]] == "\\":
        direction = (0, 1)
    move_beam(direction, position)
    return len(set([x[0] for x in energized]))


if __name__ == '__main__':
    example_target = 46
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
