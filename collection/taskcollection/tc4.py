# Write a program to check whether a string has duplicate characters or not.
# Example: 'unique' → Output: Yes (since 'u' appears more than once)
n=input('enter word: ')
for i in n:
    if n.count(i)>1:
        print('yes')
        break
