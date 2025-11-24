#find HCF of 2 given no.s
num1=int(input('enter number 1: '))
num2=int(input('enter number 2: '))
i=1
hcf=0
if num1>=num2:
    while i<=num2:
        if num1%i==0 and num2%i==0:
            hcf=i
        i+=1
else:
    while i<=num1:
        if num1%i==0 and num2%i==0:
            hcf=i
        i+=1
print('HCF:',hcf)

