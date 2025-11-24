#ask for 3 angles. if sum=180, check if equilateral,scalene or isosceles
t1=int(input('enter angle 1: '))
t2=int(input('enter angle 2: '))
t3=int(input('enter angle 3: '))
tot=t1+t2+t3
if tot==180:
    if t1==t2==t3:
        print('triangle is equilateral')
    elif t1!=t2!=t3:
        print('triangle is scalene')
    else:
        print('triangle is isosceles')
else:
    print('not a triangle')
