#create a new list with multiples of 3
l=[12,34,36,33,10,11,5,6,7]
n=[]
for i in l:
    if i%3==0:
        n.append(i)
print(n)
n.insert(2,39)
