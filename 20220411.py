# After doing your laundry, you now have a bag full of socks
# to pair up and sort. Right and left socks are mirror images
# of each other. So 'ad' is paired with 'da', 'p1' with '1p', etc.
# Write code to pair and sort your socks, putiing
# leftover singles in a separate 'bag' for next time.

socks = ['lv,eb,ho,ug,da,be,se,kc,p1,ck,gu,vl,nv,ad']
socks = socks[0].split(',')
socks.sort()
pairs = []
singles = []

for sock in socks:
    str = sock[1] + sock[0]
    if str in socks:
        pairs.append([sock, str])
        socks.remove(str)
    else:
        singles.append(sock)

print('pairs =', pairs)
print('singles =', singles)