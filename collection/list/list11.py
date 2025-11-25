#find the sum of unique numbers
l=[1,1,2,4,5,5,4,57,8,1,9,2,4,3,10]
j=[]
l.sort()
# for i in range(len(l)-1):
#     if l[i]==l[i+1]:
#         continue
#     j.append(l[i])
# print(sum(j))
# print(j)
for i in l:
    if i not in j:
        j.append(i)
print(sum(j))