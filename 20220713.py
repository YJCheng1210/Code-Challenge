raw = input('input: ')
numbers = sorted([int(x) for x in raw if x.isdigit()])
sets = set(numbers)
max_frq = 0
for i in sets:
    if numbers.count(i) > max_frq:
        max_frq = numbers.count(i)
        max_num = i
        
print(f'Number occurring most often is: {max_num}. The number of occurrences is: {max_frq}.')
