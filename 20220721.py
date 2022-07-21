# Print the letter frequency of the string. Spaces don't count
# upper/lower-case are same M==m

input = 'Nobody expects the spanish inquisition'
input = input.lower()

stat = {}

for i in range(0, len(input)):
    if input[i] not in stat:
        stat[input[i]] = 0
    stat[input[i]] += 1
stat.pop(' ')
stat = sorted(stat.items(), key = lambda e:e[1], reverse=True)        # Sort by number of occurrences, in reverse order
print(stat)
