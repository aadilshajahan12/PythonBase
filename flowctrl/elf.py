#input a no. from the user and check if the last digit is multiple of 3
num=int(input('enter the number '))
tar=num%10
if tar%3==0:
    print(num,'has a digit divisible by 3')
else:
    print(num,'has last digit',tar,' which is not divisible')