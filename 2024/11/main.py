from utils import *
from collections import defaultdict
#parse_2D_grid_to_Defaultlist

#parse_numbers

def main(input: str):
    stones = {int(i): 1 for i in input.splitlines()[0].split()}
    stones = defaultdict(int, stones)
    new_stones = []
    for i in range(75):

        new_stones = defaultdict(int, {})
        for s,j in stones.items():
            if s == 0:
                new_stones[1] += j
            elif len(str(s)) % 2 == 0:
                new_stones[int(str(s)[:len(str(s))//2])] += j
                new_stones[int(str(s)[len(str(s))//2:])] += j
            else:
                new_stones[s * 2024] += j
        #if i == 10:
        #    break
        stones = new_stones.copy()

    return sum(stones.values())


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
