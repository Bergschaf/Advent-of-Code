connects = {
    "-": [[0, -1], [0, 1]],
    "|": [[-1, 0], [1, 0]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
    ".": [[0, 0], [0, 0]]
}


def move_pos(pos, direction):
    return [pos[0] + direction[0], pos[1] + direction[1]]


def main(input: str):
    input = [list(x) for x in input.splitlines()]
    s_pos = [0, 0]
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "S":
                s_pos = [i, j]
                break

    loop = []
    current_pos = s_pos

    def check_if_x_goes_to_y(x, y):
        x_pipe = connects[input[x[0]][x[1]]]
        if move_pos(x, x_pipe[0]) == y:
            return True
        elif move_pos(x, x_pipe[1]) == y:
            return True
        return False

    def check_if_x_is_next_step_to_y(x, y):
        x_pipe = connects[input[x[0]][x[1]]]
        y_pipe = connects[input[y[0]][y[1]]]
        if move_pos(x, x_pipe[0]) == y or move_pos(x, x_pipe[1]) == y:
            if move_pos(y, y_pipe[0]) == x or move_pos(y, y_pipe[1]) == x:
                return True
        return False

    # right
    def check_loop(first_pos, s_pos):
        first_connect = connects[input[first_pos[0]][first_pos[1]]]
        if move_pos(first_pos, first_connect[0]) != s_pos and move_pos(first_pos, first_connect[1]) != s_pos:
            return False

        current_pos = first_pos

        def get_other(x):
            if x == 0:
                return 1
            return 0

        loop = [s_pos]
        while True:
            loop.append(current_pos)
            current_connect = connects[input[current_pos[0]][current_pos[1]]]
            new_pos_1 = move_pos(current_pos, current_connect[0])
            new_pos_2 = move_pos(current_pos, current_connect[1])
            if new_pos_1 == loop[-2]:
                new_pos = new_pos_2
            elif new_pos_2 == loop[-2]:
                new_pos = new_pos_1
            else:
                return False

            if new_pos == s_pos:
                return loop
            elif new_pos in loop:
                return False

            current_pos = new_pos

    x = check_loop(move_pos(s_pos, [1, 0]), s_pos)
    if not x:
        x = check_loop(move_pos(s_pos, [-1, 0]), s_pos)
    if not x:
        x = check_loop(move_pos(s_pos, [0, 1]), s_pos)
    if not x:
        x = check_loop(move_pos(s_pos, [0, -1]), s_pos)
    loop = x
    grid = []
    for i in range(len(input)):
        grid.append([])
        for j in range(len(input[i])):
            if input[i][j] == "S":
                grid[i].append(True)
            elif [i, j] in x:
                grid[i].append(True)
            else:
                grid[i].append(False)

    def reachable_pos(pos, reachable):
        moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # if p touches the edge, return True
        if pos[0] == 0 or pos[0] == len(grid) - 1 or pos[1] == 0 or pos[1] == len(grid[0]) - 1:
            return True
        for m in moves:
            new_pos = move_pos(pos, m)
            if not grid[new_pos[0]][new_pos[1]]:
                if new_pos not in reachable:
                    reachable.append(new_pos)
                    reachable = reachable_pos(new_pos, reachable)
                    if reachable is True:
                        return True
        return reachable

    enclosed = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if not grid[i][j]:
                r = reachable_pos([i, j], [])
                if r != True:
                    input[i][j] = "X"
                    enclosed += 1

    for i in range(len(input)):
        for j in range(len(input[i])):
            if grid[i][j]:
                input[i][j] = "O"

    for i in input:
        print("".join(i))
    return enclosed


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
