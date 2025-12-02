from utils import *

#parse_2D_grid_to_Defaultlist

#parse_numbers

class Dir:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

def num_keypad_pos(num: int) -> Tuple[int, int]:
    """
    A ist -1
    :param num:
    :return:
    """
    match num:
        case 1: return 0, 0
        case 2: return 0, 1
        case 3: return 0, 2
        case 4: return 1, 0
        case 5: return 1, 1
        case 6: return 1, 2
        case 7: return 2, 0
        case 8: return 2, 1
        case 9: return 2, 2
        case 0: return 3, 1
        case -1:return 3, 2

def num_keypad_path(num1, num2):





def main(input: str):



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
