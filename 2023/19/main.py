import ast

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
            lam = eval(f"lambda {variable}: {condition}")
            functions.append((variable, lam, res))
        workflow_functions[name] = (functions, default)

    def run_workflow(name, x, m, a, s):
        functions, default = workflow_functions[name]
        for variable, f, res in functions:
            var = x
            if variable == "m":
                var = m
            elif variable == "a":
                var = a
            elif variable == "s":
                var = s
            if f(var):
                if type(res) == bool:
                    return res
                return run_workflow(res, x, m, a, s)

        if type(default) == bool:
            return default
        return run_workflow(default, x, m, a, s)

    accepted = 0
    for part in parts:
        part = part[1:-1].split(",")
        nums = []
        for p in part:
            nums.append(int(p.split("=")[1]))
        if run_workflow("in", *nums):
            accepted += sum(nums)
    return accepted


if __name__ == '__main__':
    example_target = 19114
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
