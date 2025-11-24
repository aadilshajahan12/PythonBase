#WAP sum of all odd no.s
l=[1,13,4,6,11,151,12]
sum=0
for i in l:
    if i%2!=0:
        sum+=i
print(sum)