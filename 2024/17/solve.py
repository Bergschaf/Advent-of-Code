
from z3 import *


A = BitVec("x", 16)
s = Solver()
s.add(2== ((((A % 8) ^ 5) ^ 6) ^ (Int2BV(BV2Int(A) / (2 ** BV2Int(A % 8)),16))) % 8)
# solve for all solutions
print(solve((2== ((((A % 8) ^ 5) ^ 6) ^ (A / Int2BV((2 ** BV2Int(A % 8)),16))) % 8)))