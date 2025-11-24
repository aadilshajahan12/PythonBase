#largest among 3 using nestedif
num1=int(input('enter num1 '))
num2=int(input('enter num2 '))
num3=int(input('enter num3 '))
if num1==num2==num3:
    print('all are equal')
else:
    if num1 >= num2:
         if num1 > num3:
             print(num1, ' is the largest')
         else:
             print(num3, ' is the largest')
    elif num2 >= num1:
        if num2 > num3:
         print(num2, 'is the largest')
        else:
            print(num3, ' is the largest')
