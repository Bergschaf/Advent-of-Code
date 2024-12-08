from utils import *
import math
#parse_2D_grid_to_Defaultlist

#parse_numbers

def main(input: str):
    input = parse_2D_grid_to_Defaultlist(input, None)
    antennas = [] # (letter, x ,y)
    for y in range(len(input)):
        for x in range(len(input[y])):
            if input[y][x] != ".":
                antennas.append((input[y][x], x, y))
    antinodes = set()
    def is_in_bounds(x, y):
        return 0 <= x < len(input[0]) and 0 <= y < len(input)
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            if antennas[i][0] == antennas[j][0]:
                vector = (antennas[j][1] - antennas[i][1], antennas[j][2] - antennas[i][2])
                new_pos1 = (antennas[i][1], antennas[i][2])
                vector1 = vector
                while True:
                    new_pos1 = (new_pos1[0] + vector1[0], new_pos1[1] + vector1[1])
                    if is_in_bounds(*new_pos1):
                        antinodes.add(new_pos1)
                    else:
                        break
                new_pos1 = (antennas[j][1], antennas[j][2])
                while True:
                    new_pos1 = (new_pos1[0] - vector1[0], new_pos1[1] - vector1[1])
                    if is_in_bounds(*new_pos1):
                        antinodes.add(new_pos1)
                    else:
                        break
    return len(antinodes)



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
