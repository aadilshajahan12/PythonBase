#check if a given no. is palindrome
# num=int(input('enter the number: '))
# og=0
# temp=num
# while num>0:
#     og=og*10+num%10
#     num//=10
# if og==temp:
#     print('number is palindrome')
# else:
#     print('number is not palindrome')

num=int(input('enter the number: '))
temp=0
og=num
for i in range(og):
    if num!=0:
        temp=temp*10+num%10
        num//=10
        if temp==og:
            print(og,'is palindrome')
if temp!=og:
    print(og,'is not palindrome')


