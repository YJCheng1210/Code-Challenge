eggs =['r2', 'g1', 'y2', 'r3', 'g3', 'r1', 'y1', 'g2', 'y3']

eggs.sort(key = lambda s: s[0])

eggs.sort(key = lambda s: s[1])

baskets = []

for i in range(0, len(eggs), 3):
    baskets.append([eggs[i], eggs[i+1], eggs[i+2]])

print(baskets)
