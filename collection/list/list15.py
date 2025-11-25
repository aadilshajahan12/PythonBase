#check if a given string is palindrome
s=input('enter a word')
if s==s[::-1]:
    print('palindrome')
else:
    print('not')
