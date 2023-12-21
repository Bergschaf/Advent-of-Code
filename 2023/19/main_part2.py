import ast
from functools import cache, reduce
from utils import *


def main(input: str):
    workflows, parts = input.split("\n\n")
    workflows, parts = workflows.split("\n"), parts.split("\n")

    workflow_functions = {}
    for workflow in workflows:
        name, function = workflow.split("{")
        function = function[:-1].split(",")
        default = function[-1]
        if default in "AR":
            default = True if default == "A" else False
        function = function[:-1]
        functions = []
        for f in function:
            condition, res = f.split(":")
            res = (True if res == "A" else False) if res in "AR" else res
            variable = condition[0]
            cond_type = "<" in condition  # True if < else False
            value = int(condition[2:])
            functions.append((variable, cond_type, value, res))
        workflow_functions[name] = (functions, default)

    def num_combinations_in_num_list(nums):
        return reduce(lambda x, y: x * y, [x[1] - x[0] for x in nums])

    def run_workflow(name, nums):
        # nums [(xmin, xmax), ...]
        print(name, nums)
        functions, default = workflow_functions[name]
        accepted = 0
        for variable, cond_type, value, res in functions:
            var = nums["xmas".index(variable)]
            if cond_type:
                if var[1] < value:
                    if type(res) == bool:
                        return res * num_combinations_in_num_list(nums) + accepted
                    return run_workflow(res, nums) + accepted
                elif var[0] > value:
                    continue
                else:
                    new_lower = (var[0], value - 1)
                    new_upper = (value, var[1])
                    new_nums = nums.copy()
                    new_nums["xmas".index(variable)] = new_lower
                    nums["xmas".index(variable)] = new_upper
                    if type(res) == bool:
                        accepted += res * num_combinations_in_num_list(new_nums)
                    else:
                        accepted += run_workflow(res, new_nums)
            else:
                if var[0] > value:
                    if type(res) == bool:
                        return res * num_combinations_in_num_list(nums) + accepted
                    return run_workflow(res, nums) + accepted
                elif var[1] < value:
                    continue
                else:
                    new_lower = (var[0], value)
                    new_upper = (value + 1, var[1])
                    new_nums = nums.copy()
                    new_nums["xmas".index(variable)] = new_upper
                    nums["xmas".index(variable)] = new_lower
                    if type(res) == bool:
                        accepted += res * num_combinations_in_num_list(new_nums)
                    else:
                        accepted += run_workflow(res, new_nums)
        if type(default) == bool:
            return default * num_combinations_in_num_list(nums) + accepted
        return run_workflow(default, nums) + accepted

    return run_workflow("in", [(1, 4000), (1, 4000), (1, 4000), (1, 4000)])


if __name__ == '__main__':
    example_target = 167409079868000
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
