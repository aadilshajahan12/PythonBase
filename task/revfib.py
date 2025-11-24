# 1.Print all the Fibonacci numbers below n in reverse order
n=int(input('enter range: '))
f=0
s=1
for i in range(n-2):
    t=f+s
    f=s
    s=t
while(s>0):
    print(s)
    t=s-f
    s=f
    f=t
print(s)