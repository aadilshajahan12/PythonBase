#find LCM of 2 given no.s
num1=int(input('enter number 1: '))
num2=int(input('enter number 2: '))
i=2
hcf=0
lcm=0
while i<num2 and i<num1:
        mult=num2*i
        if mult%num1==0 and mult%num2==0:
            print('LCM: ',mult)
            i=num1
        i+=1
#     if num1%i==0 and num2%i==0:
#         hcf=i
#     lcm=(num1*num2)/hcf
#     i+=1
# print('LCM :',int(lcm))



