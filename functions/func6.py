def calc(c,num1,num2):
    if c==1:
        return 'addition=',num1+num2
    elif c==2:
        return 'subtraction=',num1-num2
    elif c==3:
        return 'multiplication=',num1*num2
    else:
        if num2==0:
            return 'division not possible'
        else:
            return 'division=',num1/num2
while True:
    print('****MENU**** \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Exit')
    c=int(input('enter choice: '))
    if c<5 and c>0:
        num1=int(input('enter number 1: '))
        num2=int(input('enter number 2: '))
        dec,tot=calc(c,num1,num2)
        print(dec,tot)
    elif c==5:
        print('thank you!! Visit Again.')
        break
    else:
        print('Wrong choice! Please enter a number between 1 and 5.')
    print()
# while 1:
#     print('****MENU****')
#     print('1.Addition')
#     print('2.Subtraction')
#     print('3.Multiplication')
#     print('4.Division')
#     print('5.Exit')
#     c=int(input('enter choice: '))
#     if 0<c<5:
#      num1=int(input('enter number 1: '))
#      num2=int(input('enter number 2: '))
#      if c==1:
#          print('Addition=',num1+num2)
#      elif c==2:
#          print('Subtraction=',num1-num2)
#      elif c==3:
#          print('Multiplication=',num1*num2)
#      else:
#          if num2==0:
#              print('Division not possible')
#          else:
#              print('Division=',num1/num2)
#     elif c==5:
#         print('thank you ! visit again')
#         break
#     else:
#         print('Wrong choice! Please enter a number between 1 and 5.')