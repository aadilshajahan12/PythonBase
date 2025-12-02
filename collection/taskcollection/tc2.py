# Write a program to find the character that appears the least number of times (excluding spaces).
# Example: 'mississippi' → 'm' appears once.
n=input('enter name: ')
l=set(n)
s=0
a=''
p=[]
for i in l:
   if n.count(i)<s or s==0:
       s=n.count(i)
       a=i
print(a)
