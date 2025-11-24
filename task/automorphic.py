num=int(input('enter the number: '))
sub=num**2
temp=num
auto=0
while num>0:
    num//=10
    auto+=1
etc=sub%(10**auto)
if etc==temp:
    print('it is automorphic')
else:
    print('it is not automorphic')

