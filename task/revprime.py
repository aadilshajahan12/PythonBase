# 3.Print first 10 prime numbers in reverse order
count=1
num=3
while True:
    for i in range(2,num):
        if num%i==0:
            break
    if i==num-1:
        count+=1
    if count==10:
        break
    num+=1
for i in range(num,1,-1):
    for j in range(2,i):
        if i%j==0:
            break
    if j==i-1:
        print(i)
print(2)