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
    boxes = {}
    for i in input:
        if "-" in i:
            a = i[:-1]
            box = hash(0, a)
            if box not in boxes:
                continue
            for b in boxes[box]:
                if b[0] == a:
                    boxes[box].remove(b)
                    break
        else:
            id, num = i.split("=")
            box = hash(0, id)
            place = None
            if box in boxes:
                for i, b in enumerate(boxes[box]):
                    if b[0] == id:
                        place = i
                        break
                if place is None:
                    boxes[box].append([id, int(num)])
                else:
                    boxes[box][place] = [id, int(num)]
            else:
                boxes[box] = [[id, int(num)]]

    su = 0
    for box in boxes.keys():
        for i, b in enumerate(boxes[box]):
            su += (box + 1) * (i+1) * b[1]

    return su


if __name__ == '__main__':
    example_target = 145
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
