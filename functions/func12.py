# 7.Password Strength Checker

# Define check_password(password)
# If length < 6 → "Weak"
# If 6–10 → "Medium"
# If > 10 → "Strong"

# def check_password(password):
#     l=0
#     for i in password:
#         l+=1
#     if l<6:
#         print('Weak')
#     elif l>=6<10:
#         print('Medium')
#     else:
#         print('Strong')
# check_password('fightclub')

def check_password(password):
    l=0
    for i in password:
        l+=1
    if l<6:
        return 'Weak'
    elif l>=6<10:
        return 'Medium'
    else:
        return 'Strong'
print(check_password('fightclub'))

