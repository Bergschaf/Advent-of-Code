def main(input: str):
    lines = input.split("\n")
    instructions = lines[0]
    lines = lines[2:]
    nodes = {}
    for l in lines:
        l = l.split("=")
        right_side = l[1].split(",")
        nodes[l[0].strip()] =  (right_side[0][2:], right_side[1][1:-1])
    starting_nodes = [x for x in nodes.keys() if x[-1] == "A"]
    instruction_location = 0
    steps = 0
    positions = starting_nodes.copy()
    print(starting_nodes)
    first = {}
    second = {}

    while any([x[-1] != "Z" for x in positions]):
        for i,p in enumerate(positions):
            if p[-1] == "Z":
                print(i,instruction_location)
                if i not in first:
                    first[i] = (instruction_location, steps)
                else:
                    if i not in second:
                        second[i] = (instruction_location, steps)

                        if len(second) == len(positions):
                            diffs = []
                            for k in second:
                                diffs.append(second[k][1] - first[k][1])
                            from math import gcd
                            lcm = 1
                            for i in diffs:
                                lcm = lcm * i // gcd(lcm, i)
                            return lcm

        steps += 1
        if instruction_location >= len(instructions):
            instruction_location = 0
        instruction = instructions[instruction_location]
        instruction_location += 1
        if instruction == "R":
            positions = [nodes[p][1] for p in positions]
        elif instruction == "L":
            positions = [nodes[p][0] for p in positions]
    return steps

if __name__ == '__main__':
    example_target = 6
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
