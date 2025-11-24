#WAP to calculate the electricity bill. accept the units
#100 nil, next 100 5/unit, after 200 10/unit
unit=int(input('enter unit consumed '))
if unit<=100:
    print('no charge')
else:
    if unit<=200:
        bill = (unit - 100) * 5
        print('charge = ',bill)
    else:
        bill=(unit-200)*10 +500
        print('charge =',bill)
