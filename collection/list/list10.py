#remove the mul of 5
l=[12,15,34,25,5,23]
# for i in l:
#     if i%5==0:
#         l.remove(i)
# print(l)

for i in range(len(l)-1,-1,-1):
    if l[i]%5==0:
        l.pop(i)
print(l)