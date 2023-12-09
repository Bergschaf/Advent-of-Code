from utils import recursive_split, all_different


def dist_traveled(race_time, hold_time):
    left_time = race_time - hold_time
    speed = hold_time
    return speed * left_time


def main(input: str):
    inp = input.split("\n")
    inp = [x.split()[1:] for x in inp]
    inp = [int("".join(inp[0])), int("".join(inp[1]))]
    possible_ways = 0
    print(inp)
    for j in range(inp[0]):
        dist = dist_traveled(inp[0], j)
        if dist > inp[1]:
            possible_ways += 1

    return possible_ways


if __name__ == '__main__':
    example_target = 71503
    with open("example.txt", "r") as f:
        example_output = main(f.read())

    if example_target is not None:
        if example_output == example_target:
            print(f"Example Output basst: {example_output}")
        else:
            print(f"example output basst nicht: {example_output} ;Target: {example_target}")
    else:
        print(f"Example Output: {example_output}")

    with open("input.txt", "r") as f:
        input_output = main(f.read())

    print(f"Output: {input_output}")
