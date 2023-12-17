from utils import *


def main(input: str):
    visited = dict()  # ((x, y): [total_heat_loss, blocks_straight : (x, y)])
    queue = []  # (x, y, total_heat_loss, blocks_straight)

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

    def check_cords(x, y, blocks_straight, up_to_now_heat_loss):
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            return
        heat_loss = up_to_now_heat_loss + grid[y][x]
        curr = (x, y, heat_loss, blocks_straight)
        if curr[:2] in visited:
            v = visited[curr[:2]]
            if curr in v:
                return
            if any(x[0] < curr[2] - 4 for x in v):
                return

        if curr in queue:
            return

        for i in range(len(queue)):
            if queue[i][2] > heat_loss:
                queue.insert(i, (x, y, heat_loss, blocks_straight))
                return
        queue.append((x, y, heat_loss, blocks_straight))
        # if (x, y) in visited:
        #    visited[(x, y)].append((total_heat_loss, blocks_straight))

    def get_neightbours(x, y, total_heat_loss, blocks_straight):
        if blocks_straight[0] < 3 and blocks_straight[0] >= 0:
            check_cords(x + 1, y, (blocks_straight[0] + 1, 0), total_heat_loss)
        if blocks_straight[0] > -3 and blocks_straight[0] <= 0:
            check_cords(x - 1, y, (blocks_straight[0] - 1, 0), total_heat_loss)

        if blocks_straight[1] < 3 and blocks_straight[1] >= 0:
            check_cords(x, y + 1, (0, blocks_straight[1] + 1), total_heat_loss)
        if blocks_straight[1] > -3 and blocks_straight[1] <= 0:
            check_cords(x, y - 1, (0, blocks_straight[1] - 1), total_heat_loss)

    curr = (0, 0, 0, (0, 0))
    queue.append(curr)
    grid = [[int(x) for x in y] for y in parse_grid(input)]
    target = (len(grid[0]) - 1, len(grid) - 1)
    print(target)
    i = 0
    while curr[:2] != target:
        curr = queue.pop(0)
        if curr[:2] in visited:
            v = visited[curr[:2]]
            if curr in v:
                continue

            visited[curr[:2]].append(curr[2:])

        else:
            visited[curr[:2]] = [curr[2:]]
        get_neightbours(*curr)
        if i % 1000 == 0:
            print(i, curr)
        i += 1

    return curr[2]
    # to high 1068


if __name__ == '__main__':
    example_target = 102
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
