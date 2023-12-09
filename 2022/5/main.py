def main(input: str):
    boxes, instructions = input.split("\n\n")
    boxes = boxes.splitlines()
    stacks = len(boxes[-1].split())
    box_arr = [[] for _ in range(stacks)]
    boxes = boxes[:-1]

    for box in boxes[::-1]:
        for s in range(stacks):
            pos = s * 4 + 1
            if box[pos] != " ":
                box_arr[s].append(box[pos])

    instructions = instructions.splitlines()
    for i in instructions:
        i = i.split()
        amount = int(i[1])
        from_stack = int(i[3]) - 1
        to_stack = int(i[5]) - 1
        box_arr[to_stack].extend(box_arr[from_stack][-amount:])
        box_arr[from_stack] = box_arr[from_stack][:-amount]
    return "".join([x[-1] for x in box_arr])

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
