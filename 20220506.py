# Print out the reverse of the number with each digit doubled
# example 426 -> (reverse) 624 -> (double) 1248

numbers = [34, 243, 659, 517, 8, 47]

def twist(num):
    num1 = 0
    while num != 0:
        num1 = num1 * 10 + (num % 10)
        num = int(num / 10)
    return num1 * 2

print('The twisted numbers are:', end=' ')
for number in numbers:
    print(twist(number), end=', ')