from utils import *
import time


class Test:
    def __init__(self, arr):
        self.arr = list(arr)

    def __getitem__(self, item):
        if item < 0:
            print("Negative")
            exit()
            return "None"
        try:
            return self.arr[item]
        except:
            return "None"
    def __setitem__(self, key, value):
        self.arr[key] = value

    def count(self, item):
        return self.arr.count(item)

    def join(self):
        return "".join(self.arr)

    def __len__(self):
        return len(self.arr)

    def toList(self):
        return self.arr

    def __str__(self):
        return self.join()

    def __repr__(self):
        return self.join()

def main1(input: str):
    input = [list(i)for i in input.splitlines()]
    x = 0
    y = 0
    maxx = len(input[0])
    maxy = len(input)
    direction = "up"
    def turn_left():
        nonlocal direction
        if direction == "down":
            direction = "left"
        elif direction == "right":
            direction = "down"
        elif direction == "up":
            direction = "right"
        elif direction == "left":
            direction = "up"
    def one_forward():
        nonlocal x
        nonlocal y
        if direction == "down":
            y += 1
        elif direction == "right":
            x += 1
        elif direction == "up":
            y -= 1
        elif direction == "left":
            x -= 1
    def one_ahead():
        nonlocal x
        nonlocal y
        if direction == "down":
            return input[y+1][x]
        elif direction == "right":
            return input[y][x+1]
        elif direction == "up":
            if y-1 < 0:
                return "None"
            return input[y-1][x]
        elif direction == "left":
            if x-1 < 0:
                return "None"
            return input[y][x-1]
    for i in range(len(input)):
        if "^" in input[i]:
            x = input[i].index("^")
            y = i
            break
    input = [Test(i) for i in input]
    locations = {(x, y)}
    #input[y][x] = "X"
    def print_input():
        for i in input:
            print("".join(i.toList()))
        print()
    while True:
        try:
            if one_ahead() == "#":
                turn_left()
        except Exception as e:
            print(e)
            break
        print(x, y, direction)
        one_forward()
        locations.add((x, y))
        input[y][x] = "X"#V" if direction == "down" else "<" if direction == "left" else ">" if direction == "right" else "^"
        if x < 0 or x >= maxx or y < 0 or y >= maxy:
            break
    print_input()
    print(len(locations))
    return sum([i.count("X") for i in input])



def main(input: str):
    input = [list(i)for i in input.splitlines()]
    x = 0
    y = 0
    maxx = len(input[0])
    maxy = len(input)
    direction = "up"
    def turn_left():
        nonlocal direction
        if direction == "down":
            direction = "left"
        elif direction == "right":
            direction = "down"
        elif direction == "up":
            direction = "right"
        elif direction == "left":
            direction = "up"
    def one_forward():
        nonlocal x
        nonlocal y
        if direction == "down":
            y += 1
        elif direction == "right":
            x += 1
        elif direction == "up":
            y -= 1
        elif direction == "left":
            x -= 1
    def one_ahead():
        nonlocal x
        nonlocal y
        if direction == "down":
            return input[y+1][x]
        elif direction == "right":
            return input[y][x+1]
        elif direction == "up":
            if y-1 < 0:
                return "None"
            return input[y-1][x]
        elif direction == "left":
            if x-1 < 0:
                return "None"
            return input[y][x-1]
    for i in range(len(input)):
        if "^" in input[i]:
            x = input[i].index("^")
            y = i
            break
    input = [i for i in input]
    locations = {(x, y, direction)}
    #input[y][x] = "X"
    def print_input():
        for i in input:
            print(i)
        print()
    loops = 0
    startx, starty = x, y
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "#":
                continue
            input[i][j] = "#"
            x, y = startx, starty
            direction = "up"

            locations = {(x, y, direction)}
            while True:
                try:
                    if one_ahead() == "#":
                        turn_left()
                except Exception as e:
                    break
                one_forward()
                if (x, y, direction) in locations:
                    loops += 1
                    print(loops)
                    break
                locations.add((x, y, direction))
                if x < 0 or x >= maxx or y < 0 or y >= maxy:
                    break
            input[i][j] = "."

    return loops




if __name__ == '__main__':
    example_target = 6
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
