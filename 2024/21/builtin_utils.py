
from collections import Counter

lst = [1, 2, 3, 4, 3, 4,4, 4, 4, 5, 6, 7, 8, 9, 10, 3, 3, 2]
counter = Counter(lst)
print(counter.most_common(3)) # -> [(4, 5), (3, 4), (2, 2)]  # 4, five times, 3, four times, 2, two times
# Format [(element, count), (element, count), ...]
# top 3 most common elements

lst = lst.copy()

import heapq
print(heapq.nlargest(3, lst)) # the 3 largest elements
print(heapq.nsmallest(3, lst)) # the 3 smallest elements


# zip(lst1, lst2) -> [(lst1[0], lst2[0]), (lst1[1], lst2[1]), ...]

import itertools
s = {2,4,1,6,8,7}
#print(list(itertools.permutations(s))) # All permutations of the set
#print(list(itertools.combinations(s, 3))) # All combinations of the set of length 3