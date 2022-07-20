# you have list of all shoes in your small store [model, size]
# sort and print list of all shoes by model and size

shoes = [['B', 9], ['A', 8], ['A', 7], ['C', 9],['A', 9], ['B', 7], ['C', 8], ['B', 8]]

for list in sorted(shoes):
    print(list[0],'-',list[1])