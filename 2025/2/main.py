from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

def main1(input: str):
    intervals = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in input.splitlines()[0].split(",")]
    print(intervals)
    print([x[1] - x[0] for x in intervals])
    n = 0
    for x, y in intervals:
        for z in range(x, y+1):
            if str(z)[len(str(z))//2:] == str(z)[:len(str(z))//2]:
                print(z)
                n += z
    return n

def main(input: str):
    intervals = [(int(x.split("-")[0]), int(x.split("-")[1])) for x in input.splitlines()[0].split(",")]
    print(intervals)
    print([x[1] - x[0] for x in intervals])
    n = 0
    for x, y in intervals:
        for z in range(x, y+1):
            for j in range(1, len(str(z)) // 2 + 1):
                if len(str(z)) % j == 0:
                    #print(z, j)
                    #print([(str(z)[i * j : (i+1)*j],str(z)[(i+1) * j : (i+2) * j]) for i in range(len(str(z)) // j - 1)])
                    if all(str(z)[i * j : (i+1)*j] == str(z)[(i+1) * j : (i+2) * j] for i in range(len(str(z)) // j - 1)):
                        print(z)
                        n += z
                        break

    return n

if __name__ == '__main__':
    example_target = 4174379265
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
