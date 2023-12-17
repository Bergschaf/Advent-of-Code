from utils import *
import numpy as np


def main(input: str):
    grid = [[int(x) for x in y] for y in parse_grid(input)]

    visited = np.zeros((len(grid), len(grid[0]), 2), dtype=np.bool_)  # ((x, y): [total_heat_loss, direction])
    queue = []  # (x, y, total_heat_loss, direction)

    def compare_blocks_straight(a, b):
        """
        return True if a is bigger than b
        """
        if a[0] == 0 and b[0] == 0:
            if a[1] < 0 and b[1] < 0:
                return a[1] > b[1]
            else:
                return a[1] < b[1]
        elif a[1] == 0 and b[1] == 0:
            if a[0] < 0 and b[0] < 0:
                return a[0] > b[0]
            else:
                return a[0] < b[0]
        return False

    def sort_out_unnecessary(visited_list):
        # TODO
        return visited_list

    def check_cords(x, y, direction, up_to_now_heat_loss, i):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            return
        if not direction:
            if i < 0:
                heat_loss = up_to_now_heat_loss + sum(grid[y][x + j] for j in range(0, abs(i)))
            else:
                heat_loss = up_to_now_heat_loss + sum(grid[y][x - j] for j in range(0, i))
        else:
            if i < 0:
                heat_loss = up_to_now_heat_loss + sum(grid[y + j][x] for j in range(0, abs(i)))
            else:
                heat_loss = up_to_now_heat_loss + sum(grid[y - j][x] for j in range(0, i))
        curr = (x, y, heat_loss, direction)

        if curr[3]:
            if visited[y][x][0]:
                return
        else:
            if visited[y][x][1]:
                return

        if curr in queue:
            return

        for i in range(len(queue)):
            if queue[i][2] > heat_loss:
                queue.insert(i, (x, y, heat_loss, direction))
                return
        queue.append((x, y, heat_loss, direction))
        # if (x, y) in visited:
        #    visited[(x, y)].append((total_heat_loss, blocks_straight))

    def get_neightbours(x, y, total_heat_loss, direction):  # direction True -> left irhgt, False -> up down
        if direction:
            for i in range(4, 11):
                check_cords(x + i, y, False, total_heat_loss, i)
                check_cords(x - i, y, False, total_heat_loss, -i)
        else:
            for i in range(4, 11):
                check_cords(x, y + i, True, total_heat_loss, i)
                check_cords(x, y - i, True, total_heat_loss, -i)

    curr = (0, 0, 0, True)
    queue.append(curr)
    curr = (0, 0, 0, False)
    queue.append(curr)
    target = (len(grid[0]) - 1, len(grid) - 1)
    print(target)
    i = 0
    while curr[:2] != target:
        curr = queue.pop(0)
        x, y = curr[:2]
        if curr[3]:
            if visited[y][x][0]:
                continue
            else:
                visited[y][x][0] = True
        else:
            if visited[y][x][1]:
                continue
            else:
                visited[y][x][1] = True

        get_neightbours(*curr)
        if i % 1000 == 0:
            print(i, curr)
        i += 1

    return curr[2]
    # to high 1268


if __name__ == '__main__':
    example_target = 94
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
