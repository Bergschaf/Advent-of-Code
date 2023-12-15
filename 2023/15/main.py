from utils import *

def hash(curr, str):
    for s in str:
        o = ord(s)
        curr += o
        curr = curr * 17
        curr = curr % 256
    return curr

def main(input: str):
    input = input.split(",")
    su = 0
    for i in input:
        print(hash(0, i), i)
        su += hash(0, i)

    return su

if __name__ == '__main__':
    example_target = 1320
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
