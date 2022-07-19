from itertools import combinations

inp = [3, 4, 6, 5, 7, 6, 2, 4, 9, 8, 2]
seq = set(list(combinations(inp, 3)))
eq = (lambda x: x[0] + x[1] + x[2] == 15)
results = list(filter(eq, seq))
[list(result) for result in results]
