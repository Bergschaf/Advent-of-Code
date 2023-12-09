def is_touching(pos1, pos2):
    dist_x = abs(pos1[0] - pos2[0])
    dist_y = abs(pos1[1] - pos2[1])
    if dist_y > 1 or dist_x > 1:
        return False
    return True


def get_direction(pos1, pos2):
    dir = [0, 0]
    if pos1[0] > pos2[0]:
        dir[0] = 1
    if pos1[0] < pos2[0]:
        dir[0] = -1

    if pos1[1] > pos2[1]:
        dir[1] = 1
    if pos1[1] < pos2[1]:
        dir[1] = -1

    return dir

def main(input: str):
    lines = input.splitlines()
    positions = []
    lines = [[line.split()[0], int(line.split()[1])] for line in lines]
    head_pos = [0, 0]
    tail_positions = [[0, 0] for _ in range(10)]
    while lines:
        if lines[0][0] == "R":
            head_pos[1] += 1
        if lines[0][0] == "L":
            head_pos[1] -= 1
        if lines[0][0] == "U":
            head_pos[0] += 1
        if lines[0][0] == "D":
            head_pos[0] -= 1

        lines[0][1] -= 1
        if lines[0][1] == 0:
            lines.pop(0)

        tail_positions[0] = head_pos.copy()

        org_head_pos = head_pos.copy()

        for i in range(9):
            if not is_touching(tail_positions[i], tail_positions[i+1]):
                dir = get_direction(tail_positions[i], tail_positions[i+1])
                tail_positions[i+1][0] += dir[0]
                tail_positions[i+1][1] += dir[1]

        positions.append(tuple(tail_positions[-1]))

    return len(set(positions))


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
