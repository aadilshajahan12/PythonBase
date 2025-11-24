#1 1 1 1 1
#2 2 2 2
#3 3 3
#4 4
#5
# # s=1
# # for i in range(6,1,-1):
# #     for j in range(1,i):
# #         print(s,end=' ')
# #     s+=1
#     print()
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=' ')
    print()