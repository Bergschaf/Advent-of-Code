from utils import *

def main(input: str):
    input = input.split("\n")
    input = [list(x) for x in input]
    append_after_row = []
    append_after_col = []

    for i in range(len(input)):
        if not "#" in input[i]:
            append_after_row.append(i)

    for i in range(len(input[0])):
        if not "#" in [x[i] for x in input]:
            append_after_col.append(i)

    galaxy_positions = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "#":
                galaxy_positions.append((i, j))

    distances = 0
    for i in range(len(galaxy_positions)):
        for j in range(i + 1, len(galaxy_positions)):
            m_x = min(galaxy_positions[i][0], galaxy_positions[j][0])
            M_x = max(galaxy_positions[i][0], galaxy_positions[j][0])
            m_y = min(galaxy_positions[i][1], galaxy_positions[j][1])
            M_y = max(galaxy_positions[i][1], galaxy_positions[j][1])
            num_x_rows = 0
            for x in append_after_row:
                if x > m_x and x < M_x:
                    num_x_rows += 1

            num_y_cols = 0
            for x in append_after_col:
                if x > m_y and x < M_y:
                    num_y_cols += 1

            dist = abs(galaxy_positions[i][0] - galaxy_positions[j][0]) + abs(galaxy_positions[i][1] - galaxy_positions[j][1]) - num_x_rows - num_y_cols
            dist += num_x_rows * 1000000
            dist += num_y_cols * 1000000
            distances += dist

    return distances


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
