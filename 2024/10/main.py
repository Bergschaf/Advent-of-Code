from matplotlib.pyplot import vlines

from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers
#TODO defualt list 2d besser
def main1(input: str):
    input = parse_2D_grid_to_Defaultlist(input, [None])
    trailheads = all_pos_in_2d_list(input, 0)
    def get_positions_around(pos):
        x, y = pos
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    def get_score(trailhead, input):
        positions = [trailhead]
        reached = []
        score = 0
        while positions:
            p = positions.pop(0)
            value = input[p[0]][p[1]]
            if value == 9:
                if p in reached:
                    continue
                score += 1
                reached.append(p)
            for around in get_positions_around(p):
                try:
                    if input[around[0]][around[1]] == value + 1:
                        positions.append(around)
                except:
                    pass
        return score
    score = 0
    for trailhead in trailheads:
        print(score)
        score += get_score(trailhead, input)
    return  score

def main(input: str):
    input = parse_2D_grid_to_Defaultlist(input, [None])
    trailheads = all_pos_in_2d_list(input, 0)
    def get_positions_around(pos):
        x, y = pos
        return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    def get_score(trailhead, input):
        positions = [trailhead]
        reached = []
        score = 0
        while positions:
            p = positions.pop(0)
            value = input[p[0]][p[1]]
            if value == 9:

                score += 1
            for around in get_positions_around(p):
                try:
                    if input[around[0]][around[1]] == value + 1:
                        positions.append(around)
                except:
                    pass
        return score
    score = 0
    for trailhead in trailheads:
        print(score)
        score += get_score(trailhead, input)
    return  score

if __name__ == '__main__':
    example_target = 81
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
