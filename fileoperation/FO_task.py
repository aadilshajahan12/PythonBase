f=open(r'C:\Users\there\OneDrive\Documents\customer1.txt')
#Dancer prof, fname, lname, age
dic={}
for i in st:
    d=i.rstrip('\n').split(',')
    # if d[4]=='Dancer':
    #     print(d[1:4])

#Age above 50 fname, lname, age, prof
    # if int(d[3]) >50:
    #     print(d[1:5])
#Age range 25 to 40 fname, lname, age, prof
    # if 25<int(d[3])<40:
    #     print(d[1:5])

#india work, fname, lname, age, prof
    # if d[5]=='india':
    #     print(d[1:5])

#india work and age above 50 fname, lname, age
    # if d[5] == 'india' and int(d[3])>50:
    #     print(d[1:4])

#india work and pro Dancer fname, lname, age
    # loc=d[-1]
    # if loc=='india' and d[4]=='Dancer':
    #     print(d[1:4])

#Pilot prof fname, lname, age
    # if d[4]=='Pilot':
    #     print(d[1:4])

#Pilot prof and age above 40 fname, lname, age
    # if d[4]=='Pilot' and int(d[3])>40:
    #     print(d[1:4])

#us work fname, lname, age
    # if d[-1]=='us':
    #     print(d[1:4])

#uk work and age above 50 fname, lname, age
    # work=d[-1]
    # age=int(d[3])
    # if work=='uk' and age>50:
    #     print(d[1:4])

#Each profession count
#     if d[4] not in dic:
#        dic[d[4]]=1
#     else:
#        dic[d[4]]+=1
# print(dic)
#Each Location count
#     if d[-1] not in dic:
#         dic[d[-1]] = 1
#     else:
#         dic[d[-1]] += 1
# print(dic)
#Each Age group count
    # if d[3] not in dic:
    #     dic[d[3]] = 1
    # else:
    #     dic[d[3]] += 1
print(dic)