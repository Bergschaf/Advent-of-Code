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
        old_v = None
        old_h = None
        for x in range(1, len(grid)):
            if is_horizontal_line(x, grid):
                old_h = x * 100
                break
        for y in range(1, len(grid[0])):
            if is_vertical_line(y, grid):
                old_v = y
                break
        print(old_v, old_h)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "#":
                    grid[i][j] = "."
                else:
                    grid[i][j] = "#"
                v = None
                h = None
                zz = 0
                for x in range(1, len(grid)):
                    if is_horizontal_line(x, grid):
                        h = x * 100
                        zz = 1
                        break
                for y in range(1, len(grid[0])):
                    if is_vertical_line(y, grid):
                        zz += 1
                        v = y
                        break
                if zz == 2:
                    print("error", (h, v,",", old_h, old_v))
                if grid[i][j] == "#":
                    grid[i][j] = "."
                else:
                    grid[i][j] = "#"

                if v is not None:
                    if v != old_v:
                        vert.append(v)
                        break

                if h is not None:
                    if h != old_h:
                        hor.append(h)
                        break
                if zz== 2:
                    print("-----------------------xxx")

            else:
                continue
            break
        else:
            print("----------------------------")

    return sum(vert) + sum(hor)
    # 23236


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
