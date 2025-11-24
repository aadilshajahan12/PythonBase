# .Print the pattern
#
#       10
#       11 11
#       12  12  12
#       13  13  13  13

for i in range(10,14):
    for j in range(9,i):
        print(i,end=' ')
    print()