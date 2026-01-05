#find odd number and cube
l=[1,2,3,4,5,6,7,8,9,10]
f=list(map(lambda x:x**3,filter(lambda x:x%2!=0,l)))
print(f)