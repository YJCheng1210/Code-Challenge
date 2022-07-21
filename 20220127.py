# sort expressions - list by expression-value ('4 + 2' = 6)

expressions = [5, '4+3', '3', '2*2', '2**3', '12/6', 1, '9-4']

expressions = [[v, v] if isinstance(v,int) else [v, eval(v)] for v in expressions]

expressions = sorted(expressions, key=lambda e:e[1])

print([e[0] for e in expressions])
