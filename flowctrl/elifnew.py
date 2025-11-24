#WAP to find multiple of both 3 and 5
num=int(input('enter the number '))
if num%3==0 and num%5==0:
    print(num,'is divisible by both')
else:
    print(num,'not divisble by both')