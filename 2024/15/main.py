from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    input = input.replace("&lt;", "<")
    input = input.replace("&gt;", ">")
    Map, instructions = input.split("\n\n")
    Map = parse_2D_grid_to_Defaultlist(Map)
    instructions = "".join(instructions.split("\n"))
    def map_move(old_pos, new_pos):
        symbol = Map[old_pos[0],old_pos[1]]
        Map[old_pos[0],old_pos[1]] = "."
        Map[new_pos[0],new_pos[1]] = symbol

    def in_map(pos):
        if Map[pos] is None:
            return False
        return True

    def visualize():
        for i in range(len(Map)):
            print("".join(Map[i]))


    def move(pos, direction):
        if direction == "^":
            next_pos = lambda x,y: (x-1,y)
        elif direction == "v":
            next_pos = lambda x,y: (x+1,y)
        elif direction == "<":
            next_pos = lambda x,y: (x,y-1)
        elif direction == ">":
            next_pos = lambda x,y: (x,y+1)
        else:
            print(direction)
            raise ValueError("Invalid direction")
        org_pos = pos
        moves = [(pos, next_pos(*pos))]
        valid = False
        while True:
            if not in_map(next_pos(*pos)):
                break
            pos = next_pos(*pos)
            if Map[pos] == "#":
                break
            if Map[pos] == ".":
                valid = True
                break
            moves.append((pos, next_pos(*pos)))
        if valid:
            for m in moves[::-1]:
                map_move(*m)
            return next_pos(*org_pos)
        else:
            return org_pos



    def gps(x, y):
        return x * 100 +  y

    robot_position = pos_in_2d_list(Map, "@")
    for i in instructions:
        robot_position = move(robot_position, i)

    visualize()
    box_positions = all_pos_in_2d_list(Map, "O")

    return sum([gps(*x) for x in box_positions])


def main(input: str):
    input = input.replace("&lt;", "<")
    input = input.replace("&gt;", ">")
    Map, instructions = input.split("\n\n")
    Map = Map.replace(".","..")
    Map = Map.replace("#","##")
    Map = Map.replace("O","[]")
    Map = Map.replace("@","@.")
    Map = parse_2D_grid_to_Defaultlist(Map)
    instructions = "".join(instructions.split("\n"))
    def map_move(old_pos, new_pos):
        symbol = Map[old_pos[0],old_pos[1]]
        Map[old_pos[0],old_pos[1]] = "."
        Map[new_pos[0],new_pos[1]] = symbol

    def in_map(pos):
        if Map[pos] is None:
            return False
        return True

    def visualize():
        for i in range(len(Map)):
            print("".join(Map[i]))
    visualize()

    def move(pos, direction):
        if direction == "^":
            next_pos = lambda x,y: (x-1,y)
        elif direction == "v":
            next_pos = lambda x,y: (x+1,y)
        elif direction == "<":
            next_pos = lambda x,y: (x,y-1)
        elif direction == ">":
            next_pos = lambda x,y: (x,y+1)
        else:
            print(direction)
            raise ValueError("Invalid direction")
        org_pos = pos
        moves = [(pos, next_pos(*pos))]
        valid = False
        while True:
            if not in_map(next_pos(*pos)):
                break
            pos = next_pos(*pos)
            if Map[pos] == "#":
                break
            if Map[pos] == ".":
                valid = True
                break
            if direction == "^" or direction == "v":
                if Map[pos] == "[":
                    m, _ = move((pos[0], pos[1] + 1), direction)
                    if m:
                        moves.extend(m)
                    else:
                        return [], org_pos
                elif Map[pos] == "]":
                    m, _ = move((pos[0], pos[1] - 1), direction)
                    if m:
                        moves.extend(m)
                    else:
                        return [], org_pos
            moves.append((pos, next_pos(*pos)))
        if valid:
            return moves, next_pos(*org_pos)
        else:
            return [], org_pos



    def gps(x, y):
        return x * 100 +  y

    def map_move_list(moves, direction):
        # remove doubles in moves while preserving order
        moves = list(dict.fromkeys(moves))
        if direction == "^":
            sorted_moves = moves.sort(key=lambda x: x[0])
        elif direction == "v":
            sorted_moves = moves.sort(key=lambda x: x[0], reverse=True)
        elif direction == "<":
            sorted_moves = moves.sort(key=lambda x: x[1])
        elif direction == ">":
            sorted_moves = moves.sort(key=lambda x: x[1], reverse=True)
        else:
            print(direction)
            raise ValueError("Invalid direction")
        for m in moves:
            map_move(*m)
    robot_position = pos_in_2d_list(Map, "@")
    for i in instructions:
        visualize()
        print(i)
        moves, robot_position = move(robot_position, i)

        # remove doubles in moves while preserving order
        map_move_list(moves, i)
        #if Map[robot_position] != "@":
        #    exit()
    visualize()
    box_positions = all_pos_in_2d_list(Map, "[")
    print(len(box_positions))
    return sum([gps(*x) for x in box_positions])




if __name__ == '__main__':
    example_target = 9021
    with open("example.txt", "r",encoding="utf-8") as f:
        example_output = main(f.read())

    if example_target is not None:
        if example_output == example_target:
            print(f"Example Output basst: {example_output}")
        else:
            print(f"example output basst nicht: {example_output} ;Target: {example_target}")
            exit()
    else:
        print(f"Example Output: {example_output}")

    with open("input.txt", "r",encoding="utf-8") as f:
        input_output = main(f.read())

    print(f"Output: {input_output}")
