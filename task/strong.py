num=int(input('enter the number: '))
temp=num
sub=0
sum=0
while temp>0:
    fact=1
    sub=temp%10
    temp//=10
    for i in range(1,sub+1):
        fact*=i
    sum+=fact
if sum==num:
    print('it is a strong number')
else:
    print('it is not a strong number')
