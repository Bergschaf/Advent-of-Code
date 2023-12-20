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
            res = True if res == "A" else False
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
                return res
        if type(default) == bool:
            return default
        return run_workflow(default, x, m, a, s)

    accepted = 0
    for part in parts:
        part.replace("=", ":")
        print(part)
        part_dict = ast.literal_eval(part



