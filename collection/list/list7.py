#squared according to position
l=[1,6,7,10,4,8,12]
m=[]
s=1
for i in l:
    m.append(i**s)
    s+=1
print(m)

for i in range(len(l)):
    m.append(l[i]**(i+1))
print(m)
