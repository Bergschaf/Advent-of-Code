def main(input: str):
    lines = input.splitlines()
    count = 0
    for line in lines:
        l0, l1 = line.split(",")
        l0 = l0.split("-")
        l1 = l1.split("-")
        fst = set(range(int(l0[0]), int(l0[1]) + 1))
        scd = set(range(int(l1[0]), int(l1[1]) + 1))
        if fst.issubset(scd) or scd.issubset(fst):
            count += 1
    return count


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
