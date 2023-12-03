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


if __name__ == '__main__':
    input = parse_input()
    max_cubes = [12, 13, 14]
    sum_id = 0
    for sets in input:
        if not any(any(sets[1][i][j] > max_cubes[j] for j in range(3)) for i in range(len(sets[1]))):
            sum_id += int(sets[0])
    print(sum_id)