# Write code to give correct change when someone pays for item
# in your store. Give back as few pieces of change as possible
# purchase(format): ['item', prices, payment_received]

purchases = [['Bread', 28, 50], ['Pizza', 62, 100], ['Hamburger', 39.5, 100]]

available_moneys = [100, 50, 20, 10, 5 ,2, 1, 0.5]
list1 = []

for purchase in purchases:
    item = purchase[0]
    change = purchase[2] - purchase[1]
    payments = []
    while change != 0:
        for i in range(len(available_moneys)):
            if change // available_moneys[i] >= 1:
                payments.append([int(change // available_moneys[i]), available_moneys[i]])
                change = change % available_moneys[i]

    list1.append([purchase[0], *payments])

for list in list1:
    print(list[0], end =':')
    for i in range(1, len(list)):
        print(f'{list[i][0]}x{list[i][1]}', end=',')
    print('\n')