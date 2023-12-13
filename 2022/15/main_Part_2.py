from utils import *


def main(input: str):
    input = input.split("\n")
    sensors = []  # ((x,y),(x,y))

    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for line in input:
        line = line.split(": ")
        fst = line[0].split("at ")[1].split(", ")
        fst = (int(fst[0].split("=")[1]), int(fst[1].split("=")[1]))

        scd = line[1].split("at ")[1].split(", ")
        scd = (int(scd[0].split("=")[1]), int(scd[1].split("=")[1]))

        sensors.append((fst, scd, dist(fst, scd)))

    y = 2000000
    all = set([[(x,y) for x in range(4000000)] for y in range(4000000)])
    print("all")
    covered_x = set()
    covered_y = set()
    for sensor in sensors:
        x, y = sensor[0]
        dst = sensor[2]
        covered_x.update(set(range(x - dst, x + dst)))
        covered_y.update(set(range(y - dst, y + dst)))

    max_c = 20
    m = set(range(max_c + 1))
    x = m - covered_x
    y = m - covered_y
    x, y = list(x), list(y)
    print(x, y)
    #return len(set(covered))



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
