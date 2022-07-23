# Print the words you can find in the 10X5 word matrix.
# Reading forwards or backwards.

words1 = ['holy', 'grail', 'monty', 'python',
        'life', 'of', 'brian', 'fool', 'rain']

words2 = ['liar', 'nine', 'lots', 'nary', 'near', 'rod', 'lye'
          'only', 'rail', 'hope', 'car', 'so', 'risk', 'lend']

matrix = ['nlifeloofw',
          'liargoyloh',
          'oanairbens',
          'troeasonst',
          'swgndmkdhr']

forwards = matrix.copy()
backwards = []
vertical1 = []
vertical2 = []
diagonal1 = []
diagonal2 = []

for row in matrix:
    backwards.append(row[::-1])

output1 = []
not_found1 = []
output2 = []
not_found2 = []

for w in words1:
    not_found = True
    for f in forwards:
        if w in f:
            output1.append(w)
            not_found = False
    for b in backwards:
        if w in b:
            if w not in output1:
                output1.append(w)
                not_found = False
    if not_found:
        not_found1.append(w)

print('Found: ', output1)
print('Not Found: ', not_found1)

for j in range(len(matrix[0])):
    str = ''
    for i in range(len(matrix)):
        str = str + matrix[i][j]
    vertical1.append(str)
    vertical2.append(str[::-1])

for w in words2:
    not_found = True
    for v in vertical1:
        if w in v:
            output2.append(w)
            not_found = False
    for v in vertical2:
        if w in v:
            if w not in output2:
                output2.append(w)
                not_found = False
    if not_found:
        not_found2.append(w)

for j in  range(0, 10):
    str = ''
    for i in range(0, 5):
        if (i + j < 10):
            str = str + matrix[i][i+j] 
    diagonal1.append(str)

for i in range(1, 5):
    str = ''
    for j in range(0, 4):
        str = str + matrix[i][j]
    diagonal1.append(str)

for w in words2:
    not_found = True
    for v in diagonal1:
        if w in v:
            output2.append(w)
            not_found = False
    if not_found:
        not_found2.append(w)

print('Found: ', output2)
print('Not Found: ', not_found2)