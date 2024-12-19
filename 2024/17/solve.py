from z3 import *

A = BitVec("x", 60)

out = "2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0".split(",")
out = [int(x) for x in out]

constraints = []

for x in out:
    b = A & 7
    b ^= 5
    c = A >> b
    b ^= 6
    A = A >> b
    b = b ^ c
    constraints.append(x == b & 7)

constraints.append(A == 0)
print(constraints)
solve(*constraints)

