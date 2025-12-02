# Write a program to find the character that appears the most number of times in a string.
# Example: 'banana' → 'a' appears 3 times.
n=input('enter name: ')
l=set(n)
s=0
a=''
p=[]
for i in l:
   if n.count(i)>s:
       s=n.count(i)
       a=i
print(a,'appears',s,'times')


        



