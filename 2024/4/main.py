from utils import *
import re
def main1(orginput: str):
    count = 0
    input = [i for i in orginput.splitlines()]

    for i in range(len(input)):
        res = re.findall(r"XMAS", input[i])
        count += len(res)
        res = re.findall(r"XMAS", input[i][::-1])
        count += len(res)

    input = transpose(input)
    input = ["".join(i) for i in input]
    for i in range(len(input)):
        res = re.findall(r"XMAS", input[i])
        count += len(res)
        res = re.findall(r"XMAS", input[i][::-1])
        count += len(res)

    print(count)
    class Test:
        def __init__(self, arr):
            self.arr = list(arr)
        def __getitem__(self, item):
            if item < 0:
                return None
            return self.arr[item]
        def __len__(self):
            return len(self.arr)
    input = Test([Test(i) for i in orginput.splitlines()])
    test = [list(i) for i in orginput.splitlines()]
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                try:
                    if input[i-1][j+1] == "M":
                        if input[i-2][j+2] == "A":
                            if input[i-3][j+3] == "S":
                                test[i][j] = "."
                                count += 1
                except:
                    pass

                try:
                    if input[i-1][j-1] == "M":
                        if input[i-2][j-2] == "A":
                            if input[i-3][j-3] == "S":
                                test[i][j] = "."
                                count += 1
                except:
                    pass
                try:
                    if input[i+1][j-1] == "M":
                        if input[i+2][j-2] == "A":
                            if input[i+3][j-3] == "S":
                                test[i][j] = "."
                                count += 1
                except:
                    pass
                try:
                    if input[i+1][j+1] == "M":
                        if input[i+2][j+2] == "A":
                            if input[i+3][j+3] == "S":
                                test[i][j] = "."
                                count += 1
                except:
                    pass
    print("\n".join(["".join(i) for i in test]))
    return count

def main(orginput: str):
    class Test:
        def __init__(self, arr):
            self.arr = list(arr)
        def __getitem__(self, item):
            if item < 0:
                return "None"
            try:
                return self.arr[item]
            except:
                return "None"
        def __len__(self):
            return len(self.arr)
    input = Test([Test(i) for i in orginput.splitlines()])
    count = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "A":
                try:
                    one = input[i+1][j+1] + input[i-1][j-1]
                    two = input[i+1][j-1] + input[i-1][j+1]
                    if one == "MS" or one == "SM":
                        if two == "SM" or two == "MS":
                            count += 1
                except:
                    pass
    return count


if __name__ == '__main__':
    example_target = 9
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
