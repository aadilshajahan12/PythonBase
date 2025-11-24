#WAP to find the sum of all even no.s <100 using while
# num=2
# sum=0
# while num< 100:
#     sum+=num
#     num+=2
# print(sum)

#WAP to find the SUM of odd and even no.s <100 using while
i=1
oddsum=0
evnsum=0
while i<100:
    if i%2==0:
        evnsum+=i
    else:
        oddsum+=i
    i+=1
print('odd sum= ',oddsum)
print('even sum= ',evnsum)

