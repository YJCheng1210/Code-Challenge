# You receive a partially corrupted 3 digit data string.
# Write code to clean string & sort data to list of 3 digits.

data = 'z342512?b333~h123>n<724BBB400*a'
clean = []
for s in data:
    if s.isdigit():
        clean.append(s)
str = ''
for s in clean:
    str += s
clean_data = []
for i in range(0, len(str), 3):
    clean_data.append(str[i:i+3])

print(clean_data)