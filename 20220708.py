raw = '7h15.15,a.1)a73,$parr07'
list = [ch for ch in raw if ch.isalpha()]
print(f'{len(list)} letters in string: ', end='')
for i in range(len(list)):
    print(list[i], end='')