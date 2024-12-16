from mpmath.matrices.eigen import defun

from utils import *

from collections import defaultdict
# parse_2D_grid_to_Defaultlist

# parse_numbers

def main1(input: str):
    input = parse_2D_grid_to_Defaultlist(input)
    start = pos_in_2d_list(input, "S")
    end = pos_in_2d_list(input, "E")

    def get_direction(pos1, pos2):
        if pos1[0] == pos2[0]:
            return "H"
        if pos1[1] == pos2[1]:
            return "V"
        return None

    def get_distance(path):
        score = len(path)
        for i in range(1, len(path) - 1):
            if get_direction(path[i], path[i + 1]) != get_direction(path[i - 1], path[i]):
                score += 1

    def turn_left(direction):
        if direction == (0, 1):
            return (-1, 0)
        if direction == (-1, 0):
            return (0, -1)
        if direction == (0, -1):
            return (1, 0)
        if direction == (1, 0):
            return (0, 1)

    def turn_right(direction):
        if direction == (0, 1):
            return (1, 0)
        if direction == (1, 0):
            return (0, -1)
        if direction == (0, -1):
            return (-1, 0)
        if direction == (-1, 0):
            return (0, 1)

    direction = (0, 1)
    visited = {(start)}  # (pos, distance)
    todo = [(start, direction, 0)]  # (pos, direction, distance)
    print(start, end)

    def is_valid(pos):
        return 0 <= pos[0] < len(input) and 0 <= pos[1] < len(input[0]) and input[pos[0]][pos[1]] != "#"

    def next_pos(pos, direction):
        return (pos[0] + direction[0], pos[1] + direction[1])

    while todo:
        todo = sorted(todo, key=lambda x: x[2])
        print(todo)
        pos, direction, distance = todo.pop(0)
        if pos == end:
            return distance
        visited.add(pos)
        possible = [(next_pos(pos, direction), direction, distance + 1)]
        possible.append((next_pos(pos, turn_left(direction)), turn_left(direction), distance + 1001))
        possible.append((next_pos(pos, turn_right(direction)), turn_right(direction), distance + 1001))
        for p in possible:
            if p[0] not in visited and is_valid(p[0]):
                todo.append(p)


def main(input: str):
    input = parse_2D_grid_to_Defaultlist(input)
    start = pos_in_2d_list(input, "S")
    end = pos_in_2d_list(input, "E")

    def get_direction(pos1, pos2):
        if pos1[0] == pos2[0]:
            return "H"
        if pos1[1] == pos2[1]:
            return "V"
        return None

    # TODO factor in start direction
    direction = "H"
    visited = {(start, direction)}  # (pos, distance)
    all_visited = defaultdict(lambda : dict())
    all_visited[start][direction] = 0
    todo = [(start, direction, 0)]  # (pos, direction, distance)
    distance = 0
    def is_valid(pos):
        return 0 <= pos[0] < len(input) and 0 <= pos[1] < len(input[0]) and input[pos[0]][pos[1]] != "#"

    def next_pos(pos, direction):
        if direction == "V":
            return (pos[0] + 1, pos[1]), (pos[0] - 1, pos[1])
        if direction == "H":
            return (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)

    def turn(direction):
        if direction == "V":
            return "H"
        if direction == "H":
            return "V"
        raise ValueError

    while todo:
        todo = sorted(todo, key=lambda x: x[2])
        pos, direction, distance = todo.pop(0)

        visited.add((pos, direction))
        all_visited[pos][direction] = distance
        if pos == end:
            break
        next_pos1, next_pos2 = next_pos(pos, direction)
        possible = [(next_pos1, direction, distance + 1)]
        possible.append((next_pos2, direction, distance + 1))
        possible.append((pos, turn(direction), distance + 1000))
        for p in possible:
            if p[:-1] not in visited and is_valid(p[0]):
                todo.append(p)

    def get_distance_from_pos(pos, direction):
        return min(all_visited[pos])

    path = []
    todo = [(end, direction)]

    while todo:
        #todo = sorted(todo, key=lambda x: x[2])
        pos, direction = todo.pop(0)
        path.append(pos)
        p1, p2 = next_pos(pos, direction)
        possible = [(p1, direction), (p2, direction), (pos, turn(direction))]
        for p in possible:
            if p in visited and all_visited[p[0]][p[1]] < all_visited[pos][direction]:
                if p not in todo and p not in path:
                    todo.append(p)

    # visualize
    def print_string_of_len(s, l):
        return s + " " * (l - len(s))

    for  i in range(len(input)):
        for j in range(len(input[0])):
            if (i, j) in path:
                print(print_string_of_len(str(list(all_visited[(i, j)].values())), 14), end="")
            else:
                print(print_string_of_len(input[i][j], 14), end="")
        print()
    #path = {p[0] for p in path}
    path = list(set(path))
    return len(path)









if __name__ == '__main__':
    example_target = 64
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
