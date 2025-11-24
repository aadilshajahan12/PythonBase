#read the lower from user and print all the even no.s b/w lower -100(incl)
low=int(input('enter the lower limit '))
while low<=100:
    if low%2==0:
        print(low)
        low+=2
    else:
        low+=1