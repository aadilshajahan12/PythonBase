num=int(input('enter the number: '))
sum=0
temp=num
count=1
pow=0
while temp>0:
    sum=sum*10+temp%10
    temp//=10
    count+=1
for i in range(1,count):
    l=sum%10
    pow+=l**i
    sum//=10
if pow==num:
    print(pow,'is a disarium number')
else:
    print(pow,'not a disarium number')