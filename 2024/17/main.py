from utils import *

# parse_2D_grid_to_Defaultlist

# parse_numbers

OUT = []


# registers = [a,b,c,instruction_pointer]
def combo(registers, combo):
    if combo < 4:  #
        return combo
    if combo < 7:
        return registers[combo - 4]
    raise ValueError(f"Invalid combo: {combo}")


def adv(registers, c):
    registers[0] = int(registers[0] // (2 ** combo(registers, c)))
    return registers


def bst(registers, c):
    registers[1] = combo(registers, c) % 8
    return registers


def bxl(registers, c):
    registers[1] = registers[1] ^ c
    return registers


def jnz(registers, c):
    if registers[0] != 0:
        registers[3] = c
    return registers


def bxc(registers, c):
    registers[1] = registers[1] ^ registers[2]
    return registers


def out(registers, c):
    global OUT
    OUT.append(combo(registers, c) % 8)
    return registers


def bdv(registers, c):
    registers[1] = int(registers[0] // (2 ** combo(registers, c)))
    return registers


def cdv(registers, c):
    registers[2] = int(registers[0] // (2 ** combo(registers, c)))
    return registers


opcode = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}


def run_program(registers, program):
    global OUT
    OUT = []
    while True:
        previous_program_counter = registers[3]
        if registers[3] >= len(program):
            break
        op, c = program[registers[3]], program[registers[3] + 1]
        registers = opcode[op](registers, c)
        if registers[3] == previous_program_counter:
            registers[3] += 2
    return OUT


def main(input: str, example=False):


    if example:
        return
    global OUT
    OUT = ""
    registers = []
    values = re.findall(r": (\d+)", input)
    registers.append(int(values[0]))
    registers.append(int(values[1]))
    registers.append(int(values[2]))
    registers.append(0)
    program = input.splitlines()[4].split(":")[1].split(",")
    program = [int(x) for x in program]
    print(registers)
    print(program)
    print(run_program([1000,0,0,0], program))
    exit()


    for i in range(17592186044416, 35184372088832 * 2):
        if i % 1000000 == 0:
            print(i)

        OUT = []
        registers = [i, 0, 0, 0]
        while True:
            previous_program_counter = registers[3]
            if registers[3] >= len(program):
                break
            op, c = program[registers[3]], program[registers[3] + 1]
            registers = opcode[op](registers, c)
            if registers[3] == previous_program_counter:
                registers[3] += 2

            if len(OUT) >= len(program):
                print(2 ** i, "Len Found2")
                exit()
            if OUT != program[:len(OUT)]:
                break

        if len(OUT) == len(program):
            print(i)
        if OUT == program:
            return i


if __name__ == '__main__':
    example_target = None
    with open("example.txt", "r") as f:
        example_output = main(f.read(), example=True)

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
