#1
#2 3
#4 5 6
#7 8 9 10
#11 12 13 14 15
# s=1
# for i in range(5):
#     for j in range(i+1):
#         print(s,end=' ')
#         s+=1
#     print()
for i in range(1,6):
    for j in range(1,i+1):
        print(((i*(i-1))//2)+j,end=' ')
    print()