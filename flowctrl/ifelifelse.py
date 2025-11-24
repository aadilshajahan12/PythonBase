#find the largest among two no.s print "equal" if both the no.s are same
num1=int(input("enter a number "))
num2=int(input('enter another number '))
if num1>num2:
    print(num1,'is greater than',num2)
elif num1<num2:
    print(num1,'less than',num2)
else:
    print('both are equal')
