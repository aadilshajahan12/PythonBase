#WAP to find the sum of all even and odd no.s <100
oddsum=0
evensum=0
for i in range(1,100):
    if i%2==0:
        evensum+=i
    else:
        oddsum+=i
print('odd sum:',oddsum)
print('even sum:',evensum)

