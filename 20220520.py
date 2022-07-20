# your company wants to dominate self-driving market
# write code to drive your autonomous test car sefely
# through city. Stay on righ side of the road. Start
# at top(s) and drive to (f). Don't hot 0's or left side.
# Print out the path (x) as you go along as in output example.

city = ["0000sr0000000",
        "0000rr0000000",
        "0000rr0000000",
        "0000rrrrrr000",
        "0000rrrrrr000",
        "00000000rr000",
        "00rrrrrrrr000",
        "00fr000000000"]

# Create Indexlist

co = -1
line = []
for i in city:
    for a in i:
        co += 1
        if a != '0':
            line.append(co)
            co = -1
            break
line.append(0)

# Start to drive

x = 0
street = ""
way = []
way2 = []

for i in range(len(city)):
    for a in range(len(city[i])):
        way.append(city[i][a])
    if x == 1:
        for o in range(line[i], line[i-1]+1):
            way[o] = "x"
            x = 0
    if line[i] > line[i+1]:
            way[line[i]] = "x"
            x = 1
    else:
        for o in range(line[i], line[i+1]+1):
            way[o] = "x"
    for l in way:
        street += l
    way2.append(street)
    street = ""
    way = []

# Print the Path

for row in way2:
    print(row)