# l=[[1,2,3],[4,5,6],[7,8,9]] #nested
# for i in l:
#     print(i)
#     print(i[0])
#

#create a nested list of details of 7 employees
#id , fname, last name, age ,prof,sal

l=[[101,'anandu','khilladi',22,'biker',45000],[102,'abu','sufiyan',23,'tech',35000],[103,'amal','benny',23,'wrestler',30000],
   [104,'amal','saji',21,'travel',18000],[105,'muaad','sohrab',26,'kaavadi',699],
   [106,'aman','mehroof',22,'croma',19000],[107,'john','cena',48,'actor',80000]]
to=[]
for i in l:
    # if i[3]>25:
    #     print(i)
    # if i[3]==22:
    #     print(i[1:5])
    #     if i[4]=='biker' and i[3]==22:
    #         print(i[1:4])
#     to+=i[5]
# print(to)
    to.append(i[5])
print(sum(to))