num=int(input('enter the number: '))
count=0
temp=0
duck=num
while num>0:
    temp=temp*10+num%10
    num//=10
if temp%10==0:
    print(duck,'is not a duck number')
else:
    temp//=10
    while temp>0:
        if temp%10==0:
            count+=1
        temp//=10
    if count!=0:
        print(duck,'is a duck number')
    else:
        print(duck,'not duck number')

