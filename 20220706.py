raw = [8, 7, 22, 16, 3, 24, 56, 17, 23, 6, 72]
raw = sorted(raw)
raw[1], raw[-2] = raw[-2], raw[1]
print(raw)