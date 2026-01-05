#
# 7. From [3, 6, 9, 12, 15], filter only the numbers divisible by *6* using filter and a lambda.
l= [3, 6, 9, 12, 15]
f=list(filter(lambda x:x%6==0,l))
print(f)