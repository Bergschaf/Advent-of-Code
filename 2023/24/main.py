from utils import *


def main(input: str):
    input = [x.split("@") for x in input.splitlines()]
    values = []
    for x in input:
        values.append((tuple(int(y) for y in x[0].split(",")), tuple(int(y) for y in x[1].split(","))))

    def intersection_point(pos1, pos2, v1, v2):
        m1 = v1[1] / v1[0]
        m2 = v2[1] / v2[0]
        try:
            intersection_x = (pos2[1] - pos1[1] + m1 * pos1[0] - m2 * pos2[0]) / (m1 - m2)
        except ZeroDivisionError:
            return False
        intersection_y = m1 * (intersection_x - pos1[0]) + pos1[1]
        if v1[0] > 0:
            if intersection_x < pos1[0]:
                return False
        else:
            if intersection_x > pos1[0]:
                return False

        if v2[0] > 0:
            if intersection_x < pos2[0]:
                return False
        else:
            if intersection_x > pos2[0]:
                return False

        return intersection_x, intersection_y
    test_area = ((200000000000000,400000000000000),(200000000000000,400000000000000))
    num_intersections = 0
    for i in range(len(values)):
        for j in range(i +1 , len(values)):
            intersection = intersection_point(values[i][0], values[j][0], values[i][1], values[j][1])
            if intersection:
                print(values[i], values[j], intersection)
                if intersection[0] >= test_area[0][0] and intersection[0] <= test_area[0][1] and intersection[1] >= test_area[1][0] and intersection[1] <= test_area[1][1]:
                    num_intersections += 1
    return num_intersections


    print(values)


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
