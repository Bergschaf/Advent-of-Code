from utils import *
import numpy as np


def main(input: str):
    input = input.split("\n")
    # new bool array (500,200)
    arr = np.zeros((800, 505), dtype=bool)
    floor = 0
    for line in input:
        line = line.split(" -> ")
        line = [(int((y := x.split(","))[0]), int(y[1])) for x in line]
        prev = line[0]
        if prev[1] > floor:
            floor = prev[1]
        for pos in line[1:]:
            if pos[1] > floor:
                floor = pos[1]

            if pos[0] == prev[0]:
                smaller = min(pos[1], prev[1])
                bigger = max(pos[1], prev[1])
                for i in range(smaller, bigger + 1):
                    arr[pos[0], i] = True
            elif pos[1] == prev[1]:
                smaller = min(pos[0], prev[0])
                bigger = max(pos[0], prev[0])
                for i in range(smaller, bigger + 1):
                    arr[i, pos[1]] = True
            else:
                print("ERROR")
                exit()
            prev = pos
    floor += 2
    print("floor",floor)
    def drop_one(pos):
        return pos[0], pos[1] + 1

    def drop_left(pos):
        return pos[0] - 1 , pos[1] + 1

    def drop_right(pos):
        return pos[0] + 1 , pos[1] + 1

    step = 0
    while True:
        done = False
        sand_pos = (500, 0)
        step += 1
        while True:
            if sand_pos[1] + 1 >= floor:
                arr[sand_pos] = True
                break

            if not arr[drop_one(sand_pos)]:
                sand_pos = drop_one(sand_pos)
            elif not arr[drop_left(sand_pos)]:
                sand_pos = drop_left(sand_pos)
            elif not arr[drop_right(sand_pos)]:
                sand_pos = drop_right(sand_pos)
            else:
                arr[sand_pos] = True
                if sand_pos == (500, 0):
                    done = True
                break
        if done:
            break

    #for i in range(len(arr)-1,0,-1):
    #    print(i,"".join(["#" if x else "." for x in arr[i]]))

    return step
if __name__ == '__main__':
    example_target = 93
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
