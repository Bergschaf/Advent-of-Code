DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
          "nine": "9"}

if __name__ == '__main__':
    with open("input.txt", "r") as input:
        input = input.readlines()
        sum = 0
        for line in input:
            skip = False
            for i in range(len(line)):
                if skip:
                    skip = False
                    break
                if line[i].isnumeric():
                    sum += int(line[i]) * 10
                    break
                for key in DIGITS.keys():
                    if key in line[:i + 1]:
                        sum += int(DIGITS[key]) * 10
                        skip = True
                        break

            for i in range(len(line) - 1, -1, -1):
                if skip:
                    skip = False
                    break
                if line[i].isnumeric():
                    sum += int(line[i])
                    break
                for key in DIGITS.keys():
                    if key in line[i:]:
                        sum += int(DIGITS[key])
                        skip = True
                        break

    print(sum)
