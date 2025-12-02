#word count
sen='cat rat cat cat hat'
sen=sen.split()
s=set(sen)
d={}
for i in s:
    d[i]=sen.count(i)
print(d)