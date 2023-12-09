print(sum([int([l for l in line if l.isnumeric()][0] + [l for l in line if l.isnumeric()][-1]) for line in open(
    "input.txt", "r").readlines()]))