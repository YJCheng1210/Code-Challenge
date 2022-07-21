input = 4154455441155555

input = list(str(input))
digits = [input[i:i+4] for i in range(0, len(input), 4)]

encrypt = ''

for digit in digits[:-1]:
    for element in digit:
        encrypt += '*'
    encrypt += ' '

encrypt += ''.join(digits[-1])

print('Your card: ', encrypt)


encrypt = ''

for digit in digits[:-1]:
    for element in digit:
        if int(element) != 1:
            encrypt += '*'
        else:
            encrypt += element
    encrypt += ' '

encrypt += ''.join(digits[-1])

print('Your card: ', encrypt)