from utils import *
from collections import defaultdict
#parse_2D_grid_to_Defaultlist

#parse_numbers_2D

def main1(input: str):
    input = parse_2D_grid_to_Defaultlist(input, None)
    def surrounding_four(x, y):
        return [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    regions = []
    visited = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (i,j) not in visited:
                val = input[i][j]
                new_region = [(i,j,val)]
                visited.append((i,j))
                todo = surrounding_four(i,j)
                while todo:
                    x, y = todo.pop()
                    if (x,y) in visited:
                        continue
                    if input[x,y] == val:
                        visited.append((x, y))
                        new_region.append((x,y,val))
                        todo += surrounding_four(x,y)
                regions.append(new_region)
    def get_perimeter(region):
        perimeter = 4 * len(region)
        for x, y, val in region:
            for dx, dy in surrounding_four(x, y):
                if (dx, dy, val)  in region:
                    perimeter -= 1
        return perimeter
    print(regions)
    print([get_perimeter(r) for r in regions])
    return sum(get_perimeter(r) * len(r) for  r in regions)

def main(input: str):
    input = parse_2D_grid_to_Defaultlist(input, None)
    def surrounding_four(x, y):
        return [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
    regions = []
    visited = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if (i,j) not in visited:
                val = input[i][j]
                new_region = [(i,j,val)]
                visited.append((i,j))
                todo = surrounding_four(i,j)
                while todo:
                    x, y = todo.pop()
                    if (x,y) in visited:
                        continue
                    if input[x,y] == val:
                        visited.append((x, y))
                        new_region.append((x,y,val))
                        todo += surrounding_four(x,y)
                regions.append(new_region)
    def get_continous_segments(lst):
        continuous_segments = []
        for i in range(len(lst)):
            if continuous_segments and continuous_segments[-1][-1] + 1 == lst[i]:
                continuous_segments[-1].append(lst[i])
            else:
                continuous_segments.append([lst[i]])
        return continuous_segments
    def number_of_sides(region):
        x_dir = defaultdict(list)
        y_dir = defaultdict(list)
        print(region)
        region = [(x[0],x[1]) for x in region]
        for x, y in region:
            x_dir[x].append(y)
            y_dir[y].append(x)
        sides = 0
        for x in x_dir.keys():
            continuous_segments = []
            for y in sorted(x_dir[x]):
                if continuous_segments and continuous_segments[-1][-1] + 1 == y:
                    continuous_segments[-1].append(y)
                else:
                    continuous_segments.append([y])
            # TODO check if continuous segments are sorted
            for seg in continuous_segments:
                # above
                if all(((x-1,y) not in region) for y in seg):
                    sides += 1
                else:
                    new_c = [c for c in seg if (x-1,c) not in region]
                    # count continuous segments in new_c
                    sides += len(get_continous_segments(new_c))



                # below
                if all(((x+1,y) not in region) for y in seg):
                    sides += 1
                else:
                    new_c = [c for c in seg if (x+1,c) not in region]
                    # count continuous segments in new_c
                    sides += len(get_continous_segments(new_c))

        for y in y_dir.keys():
            continuous_segments = []
            for x in sorted(y_dir[y]):
                if continuous_segments and continuous_segments[-1][-1] + 1 == x:
                    continuous_segments[-1].append(x)
                else:
                    continuous_segments.append([x])
            # TODO check if continuous segments are sorted
            continuous_segments = [sorted(c) for c in continuous_segments]
            #print(continuous_segments, input[y,y_dir[y][0]])
            for seg in continuous_segments:
                # left
                if all(((x,y-1) not in region) for x in seg):
                    sides += 1
                else:
                    new_c = [c for c in seg if (c,y-1) not in region]
                    # count continuous segments in new_c
                    sides += len(get_continous_segments(new_c))


                # right
                if all(((x,y+1) not in region) for x in seg):
                    sides += 1
                else:
                    new_c = [c for c in seg if (c,y+1) not in region]
                    # count continuous segments in new_c
                    sides += len(get_continous_segments(new_c))

        return sides


    print(regions)
    print([number_of_sides(r) for r in regions])

    return sum(number_of_sides(r) * len(r) for  r in regions)
if __name__ == '__main__':
    example_target = 1206
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
