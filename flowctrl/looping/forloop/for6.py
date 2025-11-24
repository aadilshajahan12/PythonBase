#WAP to check if a given no. is prime no.
# num=int(input('enter the number: '))
# count=0
# for i in range(2,num):
#     if(num%i==0):
#         count+=1
# if count!=0:
#     print(num,'not a prime number')
# else:
#     print(num,'is a prime number')

num=int(input('enter number'))
prime=0
for i in (2,num):
    if i!=num:
        prime=num%i
if num<1:
    print('enter number > 1')
elif num==2:
    print('prime')
elif prime==1:
    print('prime')
else:
    print('not prime')

