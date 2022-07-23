# Write code to calculate value of stocks / crypto and pordolio by combining
# data from two sources. Market contains 2020 price of stocks 

market = {'TSLA': 662, 'GOOG': 2053, 'AAPL': 122, 'FB': 291, 'NFLX': 535, 'BTC': 24000}

positions = {'FB': 15, 'GOOG': 5, 'TSLA': 9, 'AAPL': 45, 'NFLX': 12, 'BTC': 0.1}

amount = 0

str = ''

for k, v in positions.items():
    str = str + f'\n{k} {v} {int(market.get(k)*v)} USD'
    amount = amount + int(market.get(k) * v)
str = f'Stock portfolio value (2020) : {amount} USD' + str

print(str)

market_2021 = {'TSLA': 985, 'GOOG': 2965, 'AAPL': 180, 'FB': 340, 'NFLX': 595, 'BTC': 48000}

amount1 = 0
amount2 = 0
str1 = ''

for k, v in positions.items():
    x = int(market_2021.get(k)*v)
    y = int(market.get(k)*v)
    str1 = str1 + f'\n{k} {v} {x} USD'
    str1 = str1 + f', retrun = {x-y} USD'
    amount1 = amount1 + x
    amount2 = amount2 + x - y
str1 = f'\nStock portfolio value (2021) : {amount1} USD, return(2021): {amount2} USD' + str1
print(str1)