key_words = ['a', 'the', 'to']
mess = 'holy grail - the witch scence: she turned me into a newt. to a nert? it got better.'

list1 = [data for data in mess.split(' ')]
for x in key_words:
    for i in range(len(list1)-1):
        if x == list1[i]:
            print(f'{x} is surrounded by {list1[i-1]} and {list1[i+1]}')