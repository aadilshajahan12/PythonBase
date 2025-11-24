#create a list and find a total of even no.s
l=[2,3,4,6,5,77,88,9]
l1=[]
for i in l:
    if i%2==0:
        l1.append(i)
print(sum(l1))