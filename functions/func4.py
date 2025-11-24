#WAP to find or check if a given a number is even or odd
# def oe():
#     num=int(input('enter number: '))
#     if num%2==0 and num!=0:
#         print(num,'is even')
#     elif num==0:
#         print(num,'is 0')
#     else:
#         print(num,'is odd')
# oe()

# def oe(a):
#     if a % 2 == 0 and a!=0:
#         print(a,'is even')
#     elif a==0:
#         print(a,'is 0')
#     else:
#         print(a,'is odd')
# oe(0)

def oe(a):
    if a%2==0 and a!=0:
        return 'even'
    elif a%2!=0:
        return 'odd'
    else:
        return '0'
print(oe(-4))