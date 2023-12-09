from utils import recursive_split, all_different
def get_diffs(lst):
    return [lst[i] - lst[i - 1] for i in range(1, len(lst))]

def main(input: str):
    lines = input.splitlines()
    lines = [[int(x) for x in line.split()] for line in lines]
    res = []
    for line in lines:
        diffs = [line]
        while not all(x == 0 for x in diffs[-1]):
            diffs.append(get_diffs(diffs[-1]))

        placeholder = diffs[-2][-1]
        print(diffs)
        diffs.reverse()
        for diff in diffs[2:]:
            placeholder = diff[-1] + placeholder
            print(diff, placeholder)

        res.append(placeholder)

    return sum(res)




if __name__ == '__main__':
    example_target = 114
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
