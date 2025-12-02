# s={3,4,7,8}
# t={1,2,6}
# st=s.union(t)
# print(st)

s={1,2,3,4,5}
t={3,4,5,6}
st=s.union(t)
print(st)
st=s.intersection(t)
print(st)
st=s.difference(t)
print(st)
st=t.difference(s)
print(st)