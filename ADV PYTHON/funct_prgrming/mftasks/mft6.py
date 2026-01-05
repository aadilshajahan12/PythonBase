# 8. From [11, 22, 33, 44, 55], filter out all odd numbers using filter and a lambda.
l=[11, 22, 33, 44, 55]
f=list(filter(lambda x:x%2!=0,l))
print(f)