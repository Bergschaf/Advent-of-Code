def parse_input():
    with open('input.txt', 'r') as f:
        input = []
        for line in f.readlines():
            id = line.split(":")[0].split()[1]
            sets_str = line.split(":")[1].split(";")
            sets = []
            for set in sets_str:
                set = set.split(",")
                set_values = [0, 0, 0]  # r g b
                for s in set:
                    s = s.split()
                    if s[1] == "red":
                        set_values[0] = int(s[0])
                    elif s[1] == "green":
                        set_values[1] = int(s[0])
                    elif s[1] == "blue":
                        set_values[2] = int(s[0])
                sets.append(set_values)
            input.append((id, sets))
        return input

def power(set):
    return set[0] * set[1] * set[2]

if __name__ == '__main__':
    input = parse_input()
    sum_powers = 0
    for game in input:
        max_red = max(game[1][i][0] for i in range(len(game[1])))
        max_green = max(game[1][i][1] for i in range(len(game[1])))
        max_blue = max(game[1][i][2] for i in range(len(game[1])))
        max_cubes = [max_red, max_green, max_blue]
        sum_powers += power(max_cubes)

    print(sum_powers)