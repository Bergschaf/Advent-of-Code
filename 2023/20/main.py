from utils import *
from collections import defaultdict


def main(input: str):
    global low_sent, high_sent
    low_sent = 0
    high_sent = 0

    class FlipFlop:
        def __init__(self, name):
            self.name = name
            self.state = False
            self.inputs = []
            self.output = False
            self.output_connections = []

        def tick(self, block):
            print(self.name, block.name, block.output)
            if block.output:
                return

            self.output = not self.output
            global low_sent, high_sent
            for x in self.output_connections:
                if self.output:
                    high_sent += 1
                else:
                    print(low_sent)
                    low_sent += 1
                x.tick(self)

        def __repr__(self):
            return f"Flip ({self.name}) ({[x.name for x in self.inputs]})  ({[x.name for x in self.output_connections]})"

    class Conj:
        def __init__(self, name):
            self.name = name

            self.output = True
            self.last_inputs = {}
            self.inputs = []
            self.output_connections = []

            print(self.name, block.name, block.output)
            for x in self.inputs:
        def tick(self, block):
            print(self.name, block.name, block.output)
            for x in self.inputs:
                if x.name not in self.last_inputs:
                    self.last_inputs[x.name] = False

            self.last_inputs[block.name] = block.output
            if block.output:
                if not any(self.last_inputs.values()):
                    self.output = True
            else:
                self.output = False
            global low_sent, high_sent
            for x in self.output_connections:
                if self.output:
                    high_sent += 1
                else:
                    low_sent += 1
                x.tick(self)

        def __repr__(self):
            return f"Conj ({self.name}) ({[x.name for x in self.inputs]})  ({[x.name for x in self.output_connections]})"

    class Broadcaster:
        def __init__(self, name):
            self.name = name
            self.output = False
            self.output_connections = []

        def tick(self):
            global low_sent
            low_sent += 1
            for x in self.output_connections:
                x.tick(self)

        def __repr__(self):
            return "broadcast"

    blocks = {}
    inputs_not_processed = defaultdict(list)
    outputs_not_processed = defaultdict(list)
    for line in input.splitlines():
        if line.startswith("broadcaster"):
            name = "broadcaster"

            blocks["broadcaster"] = Broadcaster(name)
        elif line.startswith("%"):
            name = line[1:].split("->")[0].strip()
            blocks[name] = FlipFlop(name)
        elif line.startswith("&"):
            name = line[1:].split("->")[0].strip()
            blocks[name] = Conj(name)
        outputs = [x.strip() for x in line.split("->")[1].split(",")]
        for o in outputs:
            if o in blocks:
                blocks[name].output_connections.append(blocks[o])
                blocks[o].inputs.append(blocks[name])
            else:
                outputs_not_processed[name].append(o)
                inputs_not_processed[o].append(name)

    for name, oo in inputs_not_processed.items():
        for o in oo:
            blocks[name].inputs.append(blocks[o])

    for name, oo in outputs_not_processed.items():
        for o in oo:
            blocks[name].output_connections.append(blocks[o])


    for i in range(1000):
        blocks["broadcaster"].tick()
        print(i, low_sent, high_sent)
        exit()

    print(low_sent, high_sent)
    return low_sent * high_sent


if __name__ == '__main__':
    example_target = 1
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
