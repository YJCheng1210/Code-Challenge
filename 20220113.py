# Write code to filter & sort non-strings to new list

input = [5, 'ac', 3, 'ab', '1', 2, 'ad', '6', 4, 'aa']

new_list = [x for x in input if isinstance(x, int)]

print(sorted(new_list))

for x in input:
    if isinstance(x, str) and x.isalpha():
        input.remove(x)
new_list = [x if isinstance(x, int) else eval(x) for x in input]

print(sorted(new_list))