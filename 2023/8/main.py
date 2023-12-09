def main(input: str):
    lines = input.split("\n")
    instructions = lines[0]
    lines = lines[2:]
    nodes = {}
    for l in lines:
        l = l.split("=")
        right_side = l[1].split(",")
        nodes[l[0].strip()] =  (right_side[0][2:], right_side[1][1:-1])
    instruction_location = 0
    steps = 0
    pos = "AAA"
    while pos != "ZZZ":
        steps += 1
        if instruction_location >= len(instructions):
            instruction_location = 0
        instruction = instructions[instruction_location]
        instruction_location += 1
        if instruction == "R":
            pos = nodes[pos][1]
        elif instruction == "L":
            pos = nodes[pos][0]
    return steps

if __name__ == '__main__':
    example_target = 2
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
