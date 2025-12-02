# f=open(r'C:\Users\there\PycharmProjects\PythonCore\modpack\fileop')
# for i in f:
#     print(i)

f=open(r'C:\Users\there\OneDrive\Documents\sample.txt')
for i in f:
    i=i.rstrip('\n').split()
    if int(i[3]) >25:
        print(i[1:4])