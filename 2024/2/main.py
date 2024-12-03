from utils import *

def increasing(line):
    for i in range(len(line)):
        newline = line[:i] + line[i+1:]
        for i in range(1, len(newline)):
            if newline[i] < newline[i-1]:
                break
            if abs(newline[i] - newline[i-1]) > 3:
                break
            if newline[i] == newline[i-1]:
                break
        else:
            return True
    return False

def main(input: str):
    input = split_all_lines(input.splitlines())
    input = [[int(x) for x in line] for line in input]
    sum = 0
    for line in input:
        if increasing(line):
            sum += 1
            continue
        elif increasing(line[::-1]):
            sum += 1
            continue
    return sum



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
