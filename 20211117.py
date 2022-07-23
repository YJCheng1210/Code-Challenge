# You observe a Spectre party and log who interacts with (and knows) who
# based on data you superiors want a compiled report of who knows who.
# output format dictionary with {person:[friends],...}

interactions = [['007','Felix'],['007','Vesper'],['Vesper','Blofeld'],['Felix','Vesper'],['007','Scaramanga'],
                ['Blofeld','Chiffre'],['Mayday','007'],['Oddjob','007'],['007','Drax'],['No','Scaramanga'],
                ['Drax','Jaws'],['007','Scaramanga'],['Goldfinger','Oddjob'],['Vesper','Chiffre'],['Zorin','Mayday'],
                ['Blofeld','007'],['007','Goldfinger'],['Blofeld','Drax'],['Jaws','Drax'],['Felix','Oddjob'],
                ['Vesper','007'],['Jaws','007']]

people = []

for pair in interactions:
    people.append(pair[0])
    people.append(pair[1])

people = sorted(set(people))

friend_dict= {}

for p in people:
    friends = []
    for pair in interactions:
        if p in pair:
            for f in pair:
                if f != p:
                    friends.append(f)
    friend_dict[p] = friends

print(friend_dict)
