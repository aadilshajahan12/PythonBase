#  Write a program to find the word that occurs the most in a sentence.
# Example: "this is a test and the test" → 'test' appear twice.
n=input('enter a sentence: ')
l=n.split()
s=0
w=''
for i in l:
    if l.count(i)>s:
        s=l.count(i)
        w=i
print(f'{w} appears {s} times')