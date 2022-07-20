raw = input('input: ')

tmp_list = raw.split(',')    # split by common

print('Factors are: ', end = '')

for x in range(0, len(tmp_list)):
    number = int(tmp_list[x])
    print(f'{number} {tuple([i for i in range(1,number+1) if number%i==0])}', end = ', ')
