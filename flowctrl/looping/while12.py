#WAP to reverse a no. using while loop
num=int(input('enter the number: '))
og=0
while num>0:
    og=og*10+num%10
    num//=10
print(og)