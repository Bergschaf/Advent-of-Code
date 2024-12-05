from reportlab.lib.validators import isNumber
import re
from utils import *

def main(input: str):
    res = re.findall(r"mul\((\d+),(\d+)\)", input)
    return sum([int(x) * int(y) for x, y in res])

    res = 0
    for i in range(len(input)):
        if input[i:i+4] == "mul(":
            first_num = ""
            second_num = ""
            for j in range(i+4, len(input)):
                if input[j] == ",":
                    for k in range(j+1, len(input)):
                        if input[k] == ")":
                            res += int(first_num) * int(second_num)
                        if not isNumber(input[k]):
                            break

                        second_num += input[k]
                    break

                if not isNumber(input[j]):
                    break
                first_num += input[j]
    return res

def main2(input: str):
    res = 0
    e = True
    for i in range(len(input)):
        print(input[i:i+4])
        if input[i:i+4] == "do()":
            e = True
        if input[i:i+7] == "don't()":
            e = False
        if input[i:i+4] == "mul(" and e:
            first_num = ""
            second_num = ""
            for j in range(i+4, len(input)):
                if input[j] == ",":
                    for k in range(j+1, len(input)):
                        if input[k] == ")":
                            res += int(first_num) * int(second_num)
                        if not isNumber(input[k]):
                            break

                        second_num += input[k]
                    break

                if not isNumber(input[j]):
                    break
                first_num += input[j]
    return res



if __name__ == '__main__':
    example_target = 48
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
