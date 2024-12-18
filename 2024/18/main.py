from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str, example = False):
    width, height =( 7,7) if example else (71, 71)
    grid = [[0 for _ in range(width)] for _ in range(height)]
    for i, line in enumerate(input.splitlines()):
        if example:
            if i == 12:
                break
        else:
            if i == 1024:
                break
        x, y = line.split(",")
        x, y = int(x), int(y)
        grid[x][y] = 1
    grid = DefaultList(0, [DefaultList(0, x) for x in grid])
    todo = [((0,0), 0)]
    def get_surrounding_four(pos):
        x, y = pos
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    def is_valid(pos):
        x, y = pos
        return 0 <= x < width and 0 <= y < height and grid[pos] == 0
    visited = set()
    todoset = set()
    while True:
        #todo sort todo list by distance
        pos, dist = todo.pop(0)
        print(len(todo), pos)
        visited.add(pos)
        if pos == (width-1, height-1):
            return dist
        for new_pos in get_surrounding_four(pos):
            if is_valid(new_pos) and new_pos not in visited and new_pos not in todoset:
                todoset.add(new_pos)
                todo.append((new_pos, dist+1))
    return None


def main(input: str, example = False):
    width, height =( 7,7) if example else (71, 71)
    grid = [[0 for _ in range(width)] for _ in range(height)]
    grid = DefaultList(0, [DefaultList(0, x) for x in grid])

    for i, line in enumerate(input.splitlines()):
        x, y = line.split(",")
        x, y = int(x), int(y)
        grid[x][y] = 1
        todo = [((0,0), 0)]
        def get_surrounding_four(pos):
            x, y = pos
            return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        def is_valid(pos):
            x, y = pos
            return 0 <= x < width and 0 <= y < height and grid[pos] == 0
        visited = set()
        todoset = set()
        found = False
        print(i)

        while todo:
            #todo sort todo list by distance
            pos, dist = todo.pop(0)
            visited.add(pos)
            if pos == (width-1, height-1):
                found = True
                break
            for new_pos in get_surrounding_four(pos):
                if is_valid(new_pos) and new_pos not in visited and new_pos not in todoset:
                    todoset.add(new_pos)
                    todo.append((new_pos, dist+1))
        if not found:
            return line





if __name__ == '__main__':
    example_target = "6,1"
    with open("example.txt", "r") as f:
        example_output = main(f.read(),example=True)

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
