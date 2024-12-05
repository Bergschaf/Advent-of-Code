from utils import *
import re

def main1(input: str):
    orders = []
    pages = []
    split = input.splitlines().index("")
    for i in input.splitlines()[:split]:

        orders.append(i.split("|"))
    for i in input.splitlines()[split+1:]:
        pages.append(i.split(","))
    pages = [[int(j) for j in i] for i in pages]
    orders = [[int(j) for j in i] for i in orders]
    out = 0
    print(pages)
    print(orders)
    for i in pages:
        for j in orders:
            try:
                one = i.index(j[0])
                two = i.index(j[1])
                if two < one:
                    break
            except:
                pass
        else:
            out += int(i[len(i) // 2])

    return out



class Node:
    """
    A node in the graph, that is used in the Tarjan algorithm.
    """

    def __init__(self, name):
        self.name = name
        self.ingoing = []
        self.outgoing = []
        self.index = None
        self.lowlink = None
        self.onstack = False

    def __repr__(self):
        return str(self.name)


class Edge:
    """
    An edge between two nodes in the graph.
    """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        start.outgoing.append(self)
        end.ingoing.append(self)

    def __repr__(self):
        return f"{self.start} -> {self.end}"


def tarjan(Nodes: list[Node]) -> list[list[Node]]:
    """
    The tarjan algorithm to find the strongly connected components in a graph.
    :param Nodes: The nodes in the graph.
    :return: The strongly connected components in the graph, in topological order.
    """
    index = 0
    stack = []
    SCCs = []  # The strongly connected components

    def strongconnect(node: Node):
        """
        Breadth first search to find the strongly connected components.
        """
        nonlocal index
        node.index = index  # The node gets the next index
        node.lowlink = index  # The lowlink value is initialized with the index
        index += 1  # The index is updated for the next node
        stack.append(node)  # Push the node on the stack
        node.onstack = True  # The node is on the stack

        for e in node.outgoing:  # For all nodes that are reachable from this node
            if e.end.index is None:  # If the node has not been visited yet
                strongconnect(e.end)  # recursively visit the node
                node.lowlink = min(node.lowlink, e.end.lowlink)  # update the lowlink
            elif e.end.onstack:  # If the node is on the stack
                node.lowlink = min(node.lowlink, e.end.index)  # update the lowlink

        if node.lowlink == node.index:  # If the lowlink value is the same as the
            # index, the node is the root of a strongly connected component
            scc = []
            while True:  # All nodes in the strongly connected component are popped
                # from the stack
                w = stack.pop()
                w.onstack = False
                scc.append(w)
                if w == node:
                    break
            SCCs.append(scc)

    for v in Nodes:
        if v.index is None:  # If the node has not been visited yet
            strongconnect(v)  # Visit the node
    return SCCs


def get_nodes(filename: str) -> list[Node]:
    """
    Get the nodes from a file.
    :param filename: Filename (in the Examples directory)
    :return: The nodes in the graph.
    """
    with open(f"Examples/{filename}", "r") as f:
        lines = f.readlines()

    Nodes = {}
    Edges = []
    for l in lines[1:-1]:
        l = l.split(" < ")
        l[-1] = l[-1][0]  # remove \n
        for i in range(len(l) - 1):
            if l[i] not in Nodes:
                Nodes[l[i]] = Node(l[i])
            if l[i + 1] not in Nodes:
                Nodes[l[i + 1]] = Node(l[i + 1])
            Edges.append(Edge(Nodes[l[i]], Nodes[l[i + 1]]))
    return list(Nodes.values())

def main(input):
    orders = []
    pages = []
    split = input.splitlines().index("")
    for i in input.splitlines()[:split]:
        orders.append(i.split("|"))
    for i in input.splitlines()[split + 1:]:
        pages.append(i.split(","))
    pages = [[int(j) for j in i] for i in pages]
    orders = [[int(j) for j in i] for i in orders]
    out = 0
    wrong = []

    for i in pages:
        w = False

        for j in orders:
            try:
                one = i.index(j[0])
                two = i.index(j[1])
                if two < one:
                    w = True
            except:
                pass
        if w:
            wrong.append(i)
    res = 0
    print(wrong)
    for w in wrong:
        n = w.copy()
        e = [e for e in orders if e[0] in n and e[1] in n]
        nodes = {}
        Edges = {}
        for i in e:
            if i[0] not in nodes:
                nodes[i[0]] = Node(i[0])
            if i[1] not in nodes:
                nodes[i[1]] = Node(i[1])
            Edge(nodes[i[0]], nodes[i[1]])

        SCCs = tarjan(list(nodes.values()))
        res += SCCs[len(SCCs) // 2][0].name
    return res



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
