num=int(input('enter the number: '))
temp=num
sum=0
while temp>0:
    sum+=temp%10
    temp//=10
if num%sum==0:
    print('it is a harshad number')
else:
    print('it is not a Harshad number')
