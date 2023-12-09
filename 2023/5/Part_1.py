def convert_through_range(range: list, value: int):
    for r in range:
        if r[1] + r[2] > value >= r[1]:
            dif = value - r[1]
            return r[0] + dif
    return value


def main(input: str):
    ranges = input.split("\n\n")
    seeds = ranges[0].split(":")[1]
    seeds = [int(x) for x in seeds.split()]

    ranges = ranges[1:]
    ranges_int = []
    for r in ranges:
        r = [[int(x) for x in y.split()] for y in r.split("\n")[1:]]
        ranges_int.append(r)

    ranges = ranges_int

    end_vals = []
    for s in seeds:
        for  r in ranges:
            s = convert_through_range(r, s)
        end_vals.append(s)

    return min(end_vals)



if __name__ == '__main__':
    example_target = 35
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
