#read the lower and upper value from the user and print even no.s from the range
up=int(input('enter upper limit: '))
low=int(input('enter the lower limit: '))
for i in range(low,up+1):
    if i%2==0:
        print(i)
