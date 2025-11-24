# 2.Print the count of prime numbers in a given range.
def prime(a,b):
    if a<3:
        prime=1
        a=3
    else:
        prime=0
    for i in range(a,b+1):
        for j in range(2,i):
            if i%j==0:
                break
        if j==i-1:
            prime+=1
    print('count:',prime)
prime(1,105)
