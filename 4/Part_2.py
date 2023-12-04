with open("input.txt", "r") as f:
    total_points = 0
    scratchcards = []
    for line in f:
        line = line.split(":")[1]
        winning, have = line.split("|")
        winning = [int(x) for x in winning.split()]
        have = [int(x) for x in have.split()]
        scratchcards.append([winning, have, 1])

    for ii, sc in enumerate(scratchcards):
        matches = 0
        for i in sc[1]:
            if i in sc[0]:
                matches += 1
        for i in range(ii + 1, min(len(scratchcards), ii + matches +1)):
            scratchcards[i][2] += sc[2]

    res = 0
    for i in scratchcards:
        res += i[2]
    print(res)
