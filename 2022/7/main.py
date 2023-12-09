class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.files = []
        self.subdirs = []
        self.parent = parent

    def get_size(self):
        return sum([f.size for f in self.files]) + sum([d.get_size() for d in self.subdirs])

    def has_subdir(self, name):
        for d in self.subdirs:
            if d.name == name:
                return True
        return False

    def __repr__(self):
        return f"Dir: {self.name} {self.get_size()}"


def main(input: str):
    lines = input.splitlines()
    root = Dir("/", None)
    current_dir = root
    count = 0
    all_dirs = [root]
    while count < len(lines):
        if lines[count].startswith("$ cd"):
            name = lines[count].split()[2]
            if name == "..":
                current_dir = current_dir.parent
                count += 1
                continue
            new_dir = Dir(name, current_dir)
            all_dirs.append(new_dir)
            current_dir.subdirs.append(new_dir)
            current_dir = new_dir
            for i in range(count + 2, len(lines)):

                if lines[i].startswith("$"):
                    count = i - 2
                    break
                if not lines[i].startswith("dir"):
                    size, name = lines[i].split()
                    current_dir.files.append(File(name, int(size)))
        count += 1
    return sum([d.get_size() for d in all_dirs if d.get_size() < 100000])


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
