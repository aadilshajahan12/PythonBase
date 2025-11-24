#print all the digits of a given no.
num=int(input('enter the number: '))
og=0
while num>0:
    # print(num%10)
    # num//=10
    og=og*10+num%10
    num//=10
while og>0:
    print(og%10)
    og//=10