#cube of list
l=[1,2,3,4,5]
def s(n):
    return n**3
f=list(map(s,l))
print(f)

f=list(map(lambda n:n**3,l))
print(f)

