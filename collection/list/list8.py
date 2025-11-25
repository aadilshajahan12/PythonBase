#ask the user for a number
#check if the element is present in the list
n=int(input('enter the number: '))
l=[1,2,3,4,5,6,7,8,9,10]
if n in l:
    print('number found in list')
else:
    print('sorry number not found')