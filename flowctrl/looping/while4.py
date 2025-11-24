#read the lower and upper from user and print all the even no.s in the range of lower - upper
up=int(input('enter the upper limit '))
low=int(input('enter the lower limit '))
while low<=up:
    if low%2==0:
        print(low)
    low+=1