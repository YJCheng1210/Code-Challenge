# You are selecting art for a client with special tastes
# Client wants only to be shown art with favorite colors,
# blue(b), yellow(y), or red(r), but only one color per artpiece
# So if a piece has blue, it must not contain yellow or red.
# Write code to help you select pieces to show client.
# All art available has been color-coded by your assistant.

arts = ['1ygb', '2gbw', '3ybg', '4mbg', '5bgy', '6grb', '7yrg', '8grm', '9owy']
colors = ['b', 'y', 'r']
items = {}

for art in arts:
    frq = 0
    for color in colors:
        if color in art:
            frq += 1
    items[art] = frq

print('Artworks', end =' ')

for k, v in items.items():
    if v == 1:
        print(k[0], end=', ')

print('can be shown to client.')