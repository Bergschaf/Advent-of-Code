from utils import *


def main(input: str):
    graph = [list(x) for x in input.splitlines()]
    start = pos_in_2d_list(graph, "S")
    target = pos_in_2d_list(graph, "E")
    graph[start[0]][start[1]] = "a"
    graph[target[0]][target[1]] = "z"

    def valid_neighbours(pos, graph):
        neighbours = [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]
        for n in neighbours.copy():
            if 0 > n[0] or n[0] >= len(graph) or 0 > n[1] or n[1] >= len(graph[0]):
                neighbours.remove(n)

        self_alpha_pos = lower_alpha_index(graph[pos[0]][pos[1]])
        return [n for n in neighbours if lower_alpha_index(graph[n[0]][n[1]]) - 1 <= self_alpha_pos]

    bfs = BFS(start, target, graph, valid_neighbours)
    dist = bfs.run()
    return dist


if __name__ == '__main__':
    example_target = 31
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
