# You monitor airline passengers and have received a 'No Fly' list from authorities.
# Remember all passengers on no_fly from passenger list to creat safe list.append

passengers = ['Eric', 'Tosh', 'John', 'Ed', 'Rick', 'Michael', 'Candy', 'Terry']

no_fly = ['Johnny', 'Tosh', 'Rick', 'Ed', 'Candy', 'Roger', 'Deb', 'Tim']

safe = passengers.copy()
bumped = []

for p in safe:
    if p in no_fly:
        bumped.append(p)
        safe.remove(p)

print('safe:', safe)
print('bumped:', bumped)