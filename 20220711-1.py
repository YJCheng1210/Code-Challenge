raw1 = input('input 1: ')
raw2 = input('input 2: ')

list1 = [data.strip() for data in raw1.split(',')]
list2 = [int(data) for data in raw2.split(',')]
print(dict(zip(list1, list2)))
print('The Average =', round(sum(list2)/len(list2),2))