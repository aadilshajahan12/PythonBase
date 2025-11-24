#WAP that asks the user for their age and citizen status (y/n). if user >18, check if they are citizen. if both conditions are t print "eligible" otherwise "not"
age=int(input('enter age '))
cit=input('enter citizen status (yes/no)')
if age>=18:
    if cit == 'yes':
        print('you are eligible to vote')
    elif cit == 'no':
        print('you are not eligible to vote')
    else:
        print('invalid status')
else:
    print('not eligible to vote')
