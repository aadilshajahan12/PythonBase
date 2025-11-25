nums = [3,4,0,-2,2,-6]
v=0
for i in nums:
   if abs(i)<v or v==0:
       v=i
   if abs(v)==i:
        v=i

print(v)
