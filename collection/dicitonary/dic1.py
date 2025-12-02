#create a dix of 3 students with their marks
#add a new data
# update a value
#print downwards
# remove a value
d={'athul':23,'abhinav':21,'johns':23}
print(d)
d['anand']=22
print(d)
d['athul']=24
for i in d:
    print(i,':',d[i])
del d['abhinav']
print(d)
d.clear()
print(d)
