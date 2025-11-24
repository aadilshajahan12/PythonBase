# 3.Grade Evaluator

# Define grade(mark)
# 90-100 → "A"
# 75-89 → "B"
# 50-74 → "C"
# Below 50 → "Fail"
# Print "Your grade is {grade}"

# def grade(mark):
#     if 100>=mark>89:
#         print('your grade is A')
#     elif 90>mark>74:
#         print('your grade is B')
#     elif 75>mark>49:
#         print('your grade is c')
#     else:
#         print('your grade is Fail')
# grade(78)

def grade(mark):
    if 100>=mark>89:
        return 'A'
    elif 90>mark>74:
        return 'B'
    elif 75>mark>49:
        return 'C'
    else:
        return 'Fail'
print('your grade is',grade(77))


