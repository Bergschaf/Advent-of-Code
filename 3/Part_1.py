with open("input.txt","r") as f:
    input = f.readlines()
    parts_sum = 0

    for i in range(len(input)):
        skip_amount = 0
        for j in range(len(input[i])):
            if skip_amount > 0:
                skip_amount -= 1
                continue
            if input[i][j].isnumeric():
                last_digit = len(input[i]) - 1
                for k in range(j, len(input[i])):
                    if not input[i][k].isnumeric():
                        last_digit = k - 1
                        break

                #check if the number is a part number
                to_check = ""
                for l in range(j - 1, last_digit + 2):
                    if i > 0:
                        if 0 <= l < len(input[i - 1]):
                            to_check += input[i - 1][l]
                    if i < len(input) - 1:
                        if 0 <= l < len(input[i + 1]):
                            to_check += input[i + 1][l]
                if j > 0:
                    to_check += input[i][j - 1]
                if last_digit < len(input[i]) - 1:
                    to_check += input[i][last_digit + 1]

                for x in to_check:
                    if not x.isnumeric() and x != "." and x != "\n":
                        print(to_check)
                        break
                else:
                    print(to_check)
                    skip_amount = last_digit - j
                    continue

                parts_sum += int(input[i][j:last_digit + 1])
                #print(int(input[i][j:last_digit + 1]))
                skip_amount = last_digit - j
    print(parts_sum)

