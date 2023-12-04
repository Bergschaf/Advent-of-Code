with open("input.txt","r") as f:
    total_points = 0
    for line in f:
        line = line.split(":")[1]
        winning, have = line.split("|")
        winning = [int(x) for x in winning.split()]
        have = [int(x) for x in have.split()]
        num_matches = 0
        for h in have:
            if h in winning:
                num_matches += 1

        if num_matches != 0:
            total_points += pow(2, num_matches - 1)
    print(total_points)