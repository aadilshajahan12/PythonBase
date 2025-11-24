num=int(input('enter the number: '))
sum=0
product=1
while num>0:
    sum+=num%10
    product*=num%10
    num//=10
if sum==product:
    print('is a spy number')
else:
    print('not a spy number')