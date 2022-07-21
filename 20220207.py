# Your company wants to start analyzing text-strings. As first step
# your boss has heard of Hamming distances and wants you to create 
# code to calculate them. Hamming Distance: Number of positions at
# which corresponding symbols are different, a==b >=0, a!=b =>1
# Example: TIME and MINE => 1+0+1+0 = 2

words = ['peace', 'piece', 'geese', 'tease', 'spoon']

row = [[], [], [], [], [], []]
row[0] = ['Ham-Dis', *words] 

i = 1
for x in words:
    row[i].append(x)
    for y in words:
        ham_dis = 0
        for j in range(len(x)):
            if x[j] != y[j]:
                ham_dis += 1
        row[i].append(ham_dis)
    i += 1
print(row)