# .Find the largest odd number in a given list
def more(a):
    l=len(a)
    sum=0
    for i in range(l):
        if a[i]>sum and a[i]%2!=0:
            sum=a[i]
    print(sum)
a=[12,3,5,66,77,8,93,99,4]
more(a)

