#WAP to find factorial of a no.
num=int(input('enter the number: '))
fact=1
for i in range(2,num+1):
    fact*=i
print('factorial:',fact)