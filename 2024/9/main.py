from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    input = [int(i) for i in input.splitlines()[0]]
    final = []
    for i in range(len(input)):
        if i % 2 == 1:
            for i in range(input[i]):
                final.append("None")
        else:
            for j in range(input[i]):
                final.append(i // 2)

    while "None" in final:
        if final[-1] == "None":
            final.pop()
        else:
            final[final.index("None")] = final.pop()
    return sum([i * final[i] for i in range(len(final))])
def main(input: str):
    input = [int(i) for i in input.splitlines()[0]]
    final = []
    for i in range(len(input)):
        if i % 2 == 1:
            for i in range(input[i]):
                final.append(-1)
        else:
            for j in range(input[i]):
                final.append(i // 2)


    def get_blocks(lst, value=-1):
        blocks = [] # id, size
        for i in range(len(lst)):
            if lst[i] == value:
                if i == 0 or lst[i-1] != value:
                    blocks.append([i, 1])
                else:
                    blocks[-1][1] += 1
        return blocks

    blocks = get_blocks(final)
    end = []
    while -1 in final:
        if final[-1] < 0:
            final.pop()
        else:

            num = final[-1]
            block_size = len(final) - final.index(final[-1])
            for i, b in enumerate(blocks):
                if b[0] <= len(final) - block_size and b[1] >= block_size:
                    for j in range(block_size):
                        final[b[0] + j] = final[-1]
                        final.pop()
                        end.append(-1)

                    if block_size == b[1]:
                        blocks[i] = [-1, -1]
                    else:
                        blocks[i] = [b[0] + block_size, b[1] - block_size]
                    break
            while final[-1] < 0 or final[-1] == num:
                end.append(final.pop())


    final = final + end[::-1]

    return sum([i * final[i] for i in range(len(final)) if final[i] != -1])

if __name__ == '__main__':
    example_target = 2858
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
