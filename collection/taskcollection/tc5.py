# Write a program to find the first non-repeating character in a string.
# Example: 'swiss' → Output: 'w'
#
n=input('enter a word: ')
for i in n:
    if n.count(i)==1:
        print(i)
        break