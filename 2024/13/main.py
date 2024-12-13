import re
import sympy
from sympy.abc import n, m, c
from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    input = input.splitlines()
    games = []
    for i in range(0, len(input), 4):
        b1 = re.findall(r"\d+", input[i])
        b2 = re.findall(r"\d+", input[i+1])
        pr = re.findall(r"\d+", input[i+2])
        b1 = int(b1[0]), int(b1[1])
        b2 = int(b2[0]), int(b2[1])
        pr = int(pr[0]), int(pr[1])
        games.append((b1, b2, pr))

    tokens = 0
    for game in games:
        min_tokens = float("inf")
        for i in range(101):
            for j in range(101):

                posx = game[0][0] * i + game[1][0] * j
                posy = game[0][1] * i + game[1][1] * j
                if posx == game[2][0] and posy == game[2][1]:
                    min_tokens = min(min_tokens, i * 3 + j)
        if min_tokens != float("inf"):
            tokens += min_tokens
    return tokens

def main2(input: str):
    input = input.splitlines()
    games = []
    for i in range(0, len(input), 4):
        b1 = re.findall(r"\d+", input[i])
        b2 = re.findall(r"\d+", input[i+1])
        pr = re.findall(r"\d+", input[i+2])
        b1 = int(b1[0]), int(b1[1])
        b2 = int(b2[0]), int(b2[1])
        pr = int(pr[0]) +10000000000000, int(pr[1]) + 10000000000000
        games.append((b1, b2, pr))

    # prize_x = b1_x * n + b2_x * m
    # n = (prize_x - b2_x * m) / b1_x
    # prize_y = b1_y * n + b2_y * m
    # prize_y = b1_y * ((prize_x - b2_x * m) / b1_x) + b2_y * m
    # prize_y = b1_y * (prize_x / b1_x - b2_x * m / b1_x) + b2_y * m
    # prize_y = prize_x * b1_y / b1_x - b2_x * m * b1_y / b1_x + b2_y * m
    # prize_y = prize_x * b1_y / b1_x + m * (b2_y - b2_x * b1_y / b1_x)
    # prize_y - prize_x * b1_y / b1_x = m * (b2_y - b2_x * b1_y / b1_x)
    # m = (prize_y - prize_x * b1_y / b1_x) / (b2_y - b2_x * b1_y / b1_x)

    def get_m(prize, b1, b2):
        return (prize[1] - prize[0] * b1[1] / b1[0]) / (b2[1] - b2[0] * b1[1] / b1[0])
    def get_n(prize, b1, b2, m):
        return (prize[0] - b2[0] * m) / b1[0]

    tokens = 0
    for game in games:
        m = get_m(game[2], game[0], game[1])
        n = get_n(game[2], game[0], game[1], m)
        if m.__round__(3).is_integer() and n.__round__(3).is_integer():
            print(m, n)
            tokens += m  + n *3


    return tokens

def main(input : str):
    # sympy version
    input = input.splitlines()
    games = []
    for i in range(0, len(input), 4):
        b1 = re.findall(r"\d+", input[i])
        b2 = re.findall(r"\d+", input[i + 1])
        pr = re.findall(r"\d+", input[i + 2])
        b1 = int(b1[0]), int(b1[1])
        b2 = int(b2[0]), int(b2[1])
        pr = int(pr[0]) + 10000000000000, int(pr[1]) + 10000000000000
        games.append((b1, b2, pr))
    tokens = 0
    for game in games:
        res = sympy.solve([game[0][0] * n + game[1][0] * m - game[2][0], game[0][1] * n + game[1][1] * m - game[2][1]], (n, m))
        if float(res[n]).is_integer() and float(res[m]).is_integer():
            tokens += res[m] + res[n] * 3
    return tokens

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
