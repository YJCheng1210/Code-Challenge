# Your user registeration system had a bug, which got all
# the names backwards. Write code to print names in proper
# format, before users notive problem

wrong_names = ['Yrret, Maharg, Nhoj, Yrret, Leahcim, Cire']
correct_names = wrong_names[0][::-1].lower().split(' ,')

print('Correct names are: ', end='')
for name in correct_names:
    print(name.title(), end=', ')