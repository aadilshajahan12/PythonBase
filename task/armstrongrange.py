# Find the largest Armstrong number in a given range
def arm(a,b):
    for i in range(b,a-1,-1):
        sum=0
        temp=i
        c=len(str(b))
        while temp>0:
            sum+=(temp%10)**c
            temp//=10
        if sum==i:
            print(sum)
            break
arm(153,9480)