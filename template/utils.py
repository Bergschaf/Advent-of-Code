from typing import Callable, List, Tuple

def all_different(lst: list):
    """
    Check if all elements in the list are different
    """
    return len(lst) == len(set(lst))


def recursive_split(string, *args):
    """
    Split a string recursively by multiple delimiters
    """
    if len(args) == 0:
        return [string]
    else:
        split = string.split(args[0])
        return [recursive_split(s, *args[1:]) for s in split]

def parse_input(input:str, splitters, value_positions, to_int=True):
    out = []
    last = 0
    for i in range(len(input)):
        if input[i] in splitters:
            out.append(input[last:i])
            last = i + 1
    out.append(input[last:])
    return [int(out[x]) if to_int else out[x] for x in range(len(out)) if x in value_positions]


def lower_alphabet():
    return "abcdefghijklmnopqrstuvwxyz"

def lower_alpha_index(char):
    return lower_alphabet().index(char)


def upper_alphabet():
    return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def upper_alpha_index(char):
    return upper_alphabet().index(char)

def alpha():
    return lower_alphabet() + upper_alphabet()

def alpha_index(char):
    return alpha().index(char)


def last_int(string):
    """
    Get the last integer in a string, the last integer is separated by a space
    """
    return int(string.split()[-1])


def merge(lst1, lst2, compare):
    """
    Merge two lists with a compare function
    """
    lst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if compare(lst1[i], lst2[j]):
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i < len(lst1):
        lst.extend(lst1[i:])
    if j < len(lst2):
        lst.extend(lst2[j:])
    return lst

def mergesort(lst: list, compare):
    """
    Sort a list with mergesort
    """
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = mergesort(lst[:mid], compare)
        right = mergesort(lst[mid:], compare)
        return merge(left, right, compare)



def pos_in_2d_list(lst: List, item):
    """
    Get the position of an item in a 2d list
    """
    for y, line in enumerate(lst):
        for x, char in enumerate(line):
            if char == item:
                return y, x

def all_pos_in_2d_list(lst: List, item):
    """
    Get all positions of an item in a 2d list
    """
    pos = []
    for y, line in enumerate(lst):
        for x, char in enumerate(line):
            if char == item:
                pos.append((y, x))
    return pos


def transpos(lst: List[List]):
    """
    Transpose a 2d list
    """
    return [list(x) for x in zip(*lst)]

def clone(lst: List):
    """
    Clone a n dimensional list
    """
    if type(lst[0]) is list:
        return [clone(x) for x in lst]
    else:
        return lst.copy()


class BFS:
    point_type = Tuple[int, int]
    graph_type = List[List[int]]

    @staticmethod
    def get_valid_neighbors_4(pos: tuple, _):
        return [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1)]

    @staticmethod
    def get_valid_neighbors_diag(pos: tuple, _):
        return [(pos[0] + 1, pos[1]), (pos[0] - 1, pos[1]), (pos[0], pos[1] + 1), (pos[0], pos[1] - 1),
                (pos[0] + 1, pos[1] + 1), (pos[0] + 1, pos[1] - 1), (pos[0] - 1, pos[1] + 1), (pos[0] - 1, pos[1] - 1)]

    @staticmethod
    def get_dist_dist_x_y(pos: tuple, target: tuple, _):
        return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

    def __init__(self, start: point_type, target: point_type, graph: graph_type,
                 get_valid_neighbors: Callable[[point_type, graph_type], List[point_type]] = get_valid_neighbors_4,
                 get_distance: Callable[[point_type, point_type, graph_type], float] = get_dist_dist_x_y):
        self.start = start
        self.target = target
        self.graph = graph
        self.get_valid_neighbors = get_valid_neighbors
        self.get_distance = get_distance
        self.visited = set()
        self.queue = [(start, 0)]
        self.dist = 0
        self.failed = False

    def step(self):
        if len(self.queue) == 0:
            print(self.dist)
            print("Queue is empty")
            self.failed = True
            return True
        pos, dist = self.queue.pop(0)
        self.visited.add(pos)
        if pos == self.target:
            self.dist = dist
            print("Target reached")
            return True
        for neighbor in self.get_valid_neighbors(pos, self.graph):
            if neighbor not in self.visited and neighbor not in [x[0] for x in self.queue]:
                print(neighbor)
                self.queue.append((neighbor, dist + self.get_distance(pos, neighbor, self.graph)))
        return False

    def run(self):
        while not self.step():
            pass
        return self.dist

    def get_path(self):
        self.run()
        path = []
        pos = self.target
        while pos != self.start:
            path.append(pos)
            for neighbor in self.get_valid_neighbors(pos, self.graph):
                if neighbor in self.visited and self.get_distance(neighbor, self.target, self.graph) == self.get_distance(pos, self.target, self.graph) - 1:
                    pos = neighbor
                    break
        path.append(self.start)
        return path[::-1]
