from utils import *

def concat(a, b):
    return int(str(b) + str(a))

def test(list):
    if len(list) == 1:
        return list
    else:
        t = test(list[1:])
        return [list[0] + i for i in t] + [list[0] * i for i in t] + [concat(list[0], i) for i in t]

def main1(input: str):
    input = [i.split(": ") for i in input.splitlines()]
    res = 0
    for i in input:
        m = int(i[0])
        n = [int(j) for j in i[1].split(" ")]
        results = test(n[::-1])

        if m in results:
            res += m
    return res

def main(input: str):
    input = [i.split(": ") for i in input.splitlines()]
    res = 0
    for i in input:
        m = int(i[0])
        n = [int(j) for j in i[1].split(" ")]
        results = test(n[::-1])
        print(m,n)
        print(results)
        if m in results:
            res += m
    return res




if __name__ == '__main__':
    example_target = 11387
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
