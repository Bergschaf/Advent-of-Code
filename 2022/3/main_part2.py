from utils import lower_alphabet, upper_alphabet


def prio(char):
    if char in lower_alphabet():
        return lower_alphabet().index(char) + 1
    return upper_alphabet().index(char) + 27

def main(input: str):
    lines = input.splitlines()
    prios = []
    for i in range(0, len(lines), 3):
        for j in lines[i]:
            if j in lines[i+1] and j in lines[i+2]:
                prios.append(prio(j))
                break

    return sum(prios)


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
