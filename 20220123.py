team = {'John Clesse': 'jocl', 'Eric idle': 'ecil', 'michael palin': 'mipa',
        'graham Chapman': 'grry', 'Terry Gilliam': 'teg', 'terry jones': 'TEJO'}

new_team = []

for k, v in team.items():
    x, y = k.split(' ')
    new_team.append([k.title(), x.lower()[:2]+y.lower()[:2]])

print(dict(new_team))