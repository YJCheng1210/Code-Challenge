raw1 = input('input 1: ')
raw2 = input('input 2: ')

first_names = [name.strip().split(' ')[0].upper() for name in raw1.split(',')]
last_names = [name.strip().split(' ')[1].upper() for name in raw1.split(',')]
numbers = raw2.split(',')

for i in range(len(numbers)):
    print(first_names[i][:1:]+last_names[i][:2:]+numbers[i].strip(), end=', ')
