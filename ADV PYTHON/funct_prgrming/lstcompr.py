# `l=[i for i in range(10,51)]
# print(l)
# l=[i*2 for i in range(1,21)]
# print(l)

#with one condition
# l=[i for i in range(1,51) if i%2==0]
# print(l)
#
# l=[i for i in range(1,31) if i%2!=0]
# print(l)
#
# l=[i for i in range(1,31) if i%5==0]
# print(l)
#
# l=[i**3 for i in range(1,21)if i %2!=0 ]
# print(l)
#
# l=[i for i in range(1,21) if i%2==0]
# print(sum(l))
#
# l=[i for i in range(1,21) if i%2==0 and i%5==0]
# print(l)
#
# l=[i**2 if i%2==0 else i**3 for i in range(1,21)]
# print(l)

l=[(i,'small') if i<=15 else (i,'medium') if 15<i<=35 else (i,'large') for i in range(1,51) ]
print(l)