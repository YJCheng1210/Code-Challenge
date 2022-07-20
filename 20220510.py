# A tropical paradise realtor has landplots below for sale
# ['ID', length, width] in multiples of 10 m (5 = 50m) 
# Write code to help them sort list by plot area

plot =[['A', 3, 3], ['B', 5, 2], ['C', 6, 6], ['D', 4, 8], ['E', 11, 2]]

for item in sorted(plot, key=lambda plot: plot[1]*plot[2], reverse=True):
    print (f'{item[0]}({item[1]},{item[2]})', end=', ')
