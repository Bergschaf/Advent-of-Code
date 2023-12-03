with open("input.txt","r") as f:
    input = f.readlines()
    gears_sum = 0
    possible_gears = [[[] for j in range(len(input[1]))] for i in range(len(input))]
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
                number = int(input[i][j:last_digit + 1])
                #check if the number is a part number
                to_check = ""
                for l in range(j - 1, last_digit + 2):
                    if i > 0:
                        if 0 <= l < len(input[i - 1]):
                            if input[i - 1][l] == "*":
                                possible_gears[i - 1][l].append(number)
                    if i < len(input) - 1:
                        if 0 <= l < len(input[i + 1]):
                            if input[i + 1][l] == "*":
                                possible_gears[i + 1][l].append(number)
                if j > 0:
                    if input[i][j - 1] == "*":
                        possible_gears[i][j - 1].append(number)
                if last_digit < len(input[i]) - 1:
                    if input[i][last_digit + 1] == "*":
                        possible_gears[i][last_digit + 1].append(number)
                skip_amount = last_digit - j
    for i in range(len(possible_gears)):
        for j in range(len(possible_gears[i])):
            if len(possible_gears[i][j]) == 2:
                gears_sum += possible_gears[i][j][0] * possible_gears[i][j][1]
    print(gears_sum)

