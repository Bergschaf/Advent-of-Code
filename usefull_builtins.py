import ast

x = "[1,2,3,[1,12],2]"
print(ast.literal_eval(x))



from functools import cache, reduce
# @cache vor Funktino macht memoization, gut für rekursive Funktionen (brute force)

# reduce Beispiel:
# from functools import reduce
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))