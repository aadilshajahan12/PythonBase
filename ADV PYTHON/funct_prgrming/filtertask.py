l=[1,2,3,4,5,6,7,8,9,10]
def o(n):
    if n%2==0:
        return n
m=list(filter(o,l))
print(m)

m=list(filter(lambda x:x%2==0,l))
print(m)