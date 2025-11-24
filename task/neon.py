num=int(input('enter the number: '))
sqr=num**2
sum=0
while sqr>0:
    sum+=sqr%10
    sqr//=10
if sum==num:
    print('number is neon')
else:
    print('number is not neon')