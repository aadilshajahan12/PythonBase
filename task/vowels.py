#WAP to find vowels in a given word
nam=input('enter a word: ')
for i in nam:
    if i in 'aeiouAEIOU':
        print(i.upper(),end=' ')