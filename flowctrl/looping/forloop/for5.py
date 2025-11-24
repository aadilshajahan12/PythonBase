#fibanocci series
num=int(input('enter the range: '))
# fib=0
# s=1
# for i in range(0,num):
#     t=fib+s
#     print(fib)
#     fib=s
#     s=t
f=0
t=1
for i in range(num):
     print(f)
     s=f
     f=t
     t=f+s



