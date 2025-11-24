#find largest among 3 no.s.
num1=int(input('enter number 1 '))
num2=int(input('enter number 2 '))
num3=int(input('enter number 3 '))
if num1>=num2 and num1>num3 or (num1>num2 and num1>=num3):
    print(num1,' n1 is the largest')
elif num2>num1 and num2>=num3:
    print(num2,' n2 is the largest')
elif num1==num2==num3:
    print('all are equal')
else:
    print(num3,' n3 is the largest')

