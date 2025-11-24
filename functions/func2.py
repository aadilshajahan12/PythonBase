#WAP factorial of a number using functions
# def fact():
#     num=int(input('enter number: '))
#     tot=1
#     for i in range(1,num+1):
#         tot*=i
#     print(tot)
# fact()

# def fact(a):
#     tot=1
#     for i in range(1,a+1):
#         tot*=i
#     print(tot)
# fact(4)

def fact(a):
    tot=1
    for i in range(1,a+1):
        tot*=i
    return tot
# num=int(input('enter number: '))
print(fact(int(input('enter number: '))))