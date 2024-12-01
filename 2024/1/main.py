from utils import *

def main1(input: str):
    l1, l2 = [], []
    for l in input.splitlines():
        l1.append(int(l.split(" ")[0]))
        l2.append(int(l.split(" ")[-1]))
    diffs = []
    l1 = sorted(l1)
    l2 = sorted(l2)
    for i in range(0, len(l1)):
        diffs.append(abs(l2[i] - l1[i]))
    return sum(diffs)

def main(input : str):
    l1, l2 = [], []
    for l in input.splitlines():
        l1.append(int(l.split(" ")[0]))
        l2.append(int(l.split(" ")[-1]))
    res = []
    for i in l1:
        res.append(i * l2.count(i))
    return sum(res)

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
