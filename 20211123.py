# Find the word root of the words presented

import snowballstemmer 
stemmer = snowballstemmer.stemmer("english")

words = ['plays', 'eater', 'jumps', 'jumper', 'eating', 'jumping', 'eats', 'playing', 'player']

roots = []
for w in words:
    roots.append(stemmer.stemWord(w))

root = []

for i in range(0, len(roots)):
    for j in range(i+1, len(roots)):
        if roots[i] in roots[j]:
            root.append(roots[i])

roots = [w for w in set(root)]

print(roots)

# Advanced: add the endings in a dictionary

word_dict = {}

for x in roots:
    suffix = []
    for y in words:
        if x in y:
            w1, w2 = y.split(x)
            suffix.append(w2)
    word_dict[x] = suffix

print(word_dict)

# 2 Write a function that outputs + correct ending

def word_creator(w, l):
    for s in word_dict.get(w):
        if len(s) == l:
            return w+s

print(word_creator('eat', 2))
print(word_creator('jump', 3))
