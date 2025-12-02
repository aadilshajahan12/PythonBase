#word count
f=open(r'C:\Users\there\PycharmProjects\PythonCore\modpack\news')
d={}
for i in f:
    s=i.split()
    for j in s:
        if j not in f:
            d[j]=1
        else:
            d[j]+=1
print(d)