#create a file with number, use program to read the file and add the elements into a list and find sum
n=open('namo','r')
l=[]
for i in n:
#     i=int(i)
#     l.append(i)
# print(l)
# print(sum(l))
    l.append(int(i.rstrip('\n')))
print(sum(l))