def main(input: str):
    lines = input.splitlines()
    trees = [[int(x) for x in list(line)] for line in lines]
    highest_score = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[i]) - 1):
            t = trees[i][j]
            row_right = trees[i][j + 1:]
            row_left = trees[i][:j:][::-1]
            col_up = [trees[k][j] for k in range(i)][::-1]
            col_down = [trees[k][j] for k in range(i + 1, len(trees))]
            score = 1

            def along_line(row):
                for i, r in enumerate(row):
                    if r >= t:
                        return (i + 1)
                return len(row)

            score *= along_line(row_right)
            score *= along_line(row_left)
            score *= along_line(col_up)
            score *= along_line(col_down)
            if score > highest_score:
                highest_score = score

    return highest_score


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
