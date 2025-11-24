num=int(input('enter the number: '))
temp=num
sum=0
while temp>0:
    sum+=(temp%10)**3
    temp//=10
if sum==num:
    print(num,'is an Armstrong number')
else:
    print('not an armstrong number')