l=[1,2,3,4,5]
def s(n):
    return n**2
f=list(map(s,l))
print(f)

f=list(map(lambda n:n**2,l))
print(f)

