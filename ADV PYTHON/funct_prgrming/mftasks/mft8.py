# 10. From [45, 67, 23, 90, 55], filter and print only the passing marks(greater than or equal to 50) using filter
l=[45, 67, 23, 90, 55]
f=list(filter(lambda x:x>=50,l))
print(f)