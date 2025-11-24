#create a list of elements in the range of 1-100 .
# print the main list and sum of the main list
# and find the even no.s from the given range and also find the sum of even no.s
#odd no.s and sum of odd no.s
l=[]
even=[]
odd=[]
for i in range(1,101):
    l.append(i)
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('total',l,'\n', sum(l))
print('odd',odd,sum(odd))
print('even',even,sum(even))