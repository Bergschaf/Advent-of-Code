def main(input: str):
    lines = input.splitlines()
    trees = [[int(x) for x in list(line)] for line in lines]
    visible = (len(trees[0]) - 1) * 2 + (len(trees) - 1) * 2
    for i in range(1, len(trees)-1):
        for j in range(1, len(trees[i])-1):
            t = trees[i][j]
            row_right = trees[i][j+1:]
            row_left = trees[i][:j]
            col_up = [trees[k][j] for k in range(i)]
            col_down = [trees[k][j] for k in range(i+1, len(trees))]
            if (all(r < t for r in row_right) or all(r < t for r  in row_left)
                    or all(r < t for r  in col_up) or all(r < t for r  in col_down)):
                visible += 1



    return visible


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
