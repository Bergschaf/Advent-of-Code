import numpy as np


def convert_through_range(range: np.array, value_ranges):
    # value_range: start, end
    new_ranges = []
    for r in range:
        new_value_ranges = []
        for v in value_ranges:
            print(f"range: {r}")
            print(f"value: {v}")
            if r[1] <= v[0] < r[2] + r[1]:
                print("start in range")
                # the start is in the range
                if v[1] >= r[2] + r[1]:
                    print("end not in range")
                    # the end is above in the range
                    diff = v[0] - r[1]
                    new_ranges.append((r[0] + diff, r[0] + r[2]))
                    new_value_ranges.append((r[2] + r[1], v[1]))
                else:

                    print("end in range")
                    # the end is in the range
                    diff = v[0] - r[1]
                    new_ranges.append((r[0] + diff, r[0] + diff + v[1] - v[0]))
            else:
                print("start not in range")
                # the start is not in the range
                if v[1] >= r[2] + r[1]:
                    print("end not in range (above)")
                    # the end is above in the range
                    if v[0] < r[1]:
                        print("start not in range (below)")
                        # the start is below in the range
                        new_ranges.append((r[0], r[0] + r[2]))
                        new_value_ranges.append((r[2] + r[1], v[1]))
                        new_value_ranges.append((v[0], r[1]))
                    else:
                        print("start not in range (above)")
                        # the start is above in the range
                        new_value_ranges.append(v)
                elif v[1] <= r[1]:
                    print("end not in range (below)")
                    new_value_ranges.append(v)
                else:
                    print("end in range")
                    # the end is in the range, the start must be below
                    new_ranges.append((r[0], r[0] + r[1] - v[1]))
                    new_value_ranges.append((v[0], r[1]))
            print("----")
        value_ranges = new_value_ranges.copy()

    return new_ranges + value_ranges


def main(input: str):
    ranges = input.split("\n\n")
    seeds = ranges[0].split(":")[1]
    seeds = [int(x) for x in seeds.split()]

    ranges = ranges[1:]
    ranges_int = []
    for r in ranges:
        r = [[int(x) for x in y.split()] for y in r.split("\n")[1:]]
        ranges_int.append(np.array(r))

    ranges = ranges_int
    sum = 0
    for i in range(0, len(seeds), 2):
        sum += seeds[i + 1]
    print(sum)

    end_vals = []
    for i in range(0, len(seeds), 2):
        seed_range = [(seeds[i], seeds[i + 1] + seeds[i])]
        for r in ranges:
            seed_range = convert_through_range(r, seed_range)
        end_vals.extend(seed_range)

    return min(end_vals, key=lambda x: x[0])[0]


if __name__ == '__main__':
    example_target = 46
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
