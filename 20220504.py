# Your website shows oil(CL), natural gas(NG), gold(GC) and silver(SI) prices in 'real-time'
# in fast markets. Price updates lag behind as queue overloads and users get upset.
# Current code displays all updates in order they arrived to queue. Create new queue
# handler that updates latest available price for each commodity, hopefully faster
# new prices are added to end of list, and first position is read and then removed from queue

q = ['CL,105.3', 'GC,1866.40', 'SI,22.85', 'CL,105.4', 'NG,7.525', 'CL,105.6', 'GC,1886.80', 'NG,7.535']
codes = {'CL': 'Crude Oil', 'GC': 'Gold', 'SI': 'Silver', 'NG': 'Natural Gas', }
new_q = []

for item in q:
    for item1 in new_q:
        if item1[:2] == item[:2]:
            new_q[new_q.index(item1)] = item
            break
    else:
        new_q.append(item)

print('q =', q)
print('# New queue should be')
print('new_q =', new_q)
print('# and as each price is printed out, remove that price update')

for i in range(len(new_q)):
    info = new_q.pop(0)
    code = info[:2]
    price = info[3:]
    print(f'{codes[code]}({code}) {price}, ', end ='')
    print('new_q =', new_q)