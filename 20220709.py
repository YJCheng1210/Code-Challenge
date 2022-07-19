list1 = [911, 996, 928, 944, 911, 996, 928, 356, 924]

list2 = set([data for data in list1 if list1.count(data) >= 2])

print('2 or more of: ', end = '')

for num in list2:
    print(num, end = ', ')