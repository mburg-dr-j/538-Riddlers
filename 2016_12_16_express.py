import itertools

counts = [0, 0, 0, 0, 0, 0, 0]
for perm in itertools.permutations([0,1,2,3,4,5]):
  count = 0
  for item in perm:
    if perm.index(item) == item:
      count += 1
  counts[count] += 1
print counts, sum(counts)

"""
1
0
6C2 * 1 = 15
6C3 * 2 = 40
6C4 * 3 * 3 = 135
6C5 * (4 * 1 * 2 + 4 * 3 * 3) = 264
6C6 * (5 * 1 * 3 * 3 + 5 * 4 * (1 * 2 + 3 * 3)) = 265
"""
