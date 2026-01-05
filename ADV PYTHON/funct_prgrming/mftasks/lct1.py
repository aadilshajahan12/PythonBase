# 1. Create a list [1–1000] elements
#
# 2. Find all of the numbers from 1–500 that are divisible by 7
#
# 3. Find all of the numbers from 1–300 that have 3 in them---- [3,13,23,30,31,----
l=[i for i in range(1,1001)]
# print([i for i in l if i%7==0 and i<501 ])
print([i for i in l if '3' in str(i) and i<301])
