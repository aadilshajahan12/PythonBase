# Write a program that removes all duplicate characters and returns the string with only the first occurrence kept.
# Example: 'programming' → 'progamin
p=input('enter a word: ')
s=''
for i in p:
    if i not in s:
        s+=i
print(s)