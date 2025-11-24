# 5.Age Category

# Define age_group(age)
# age < 13 → "Child"
# 13–19 → "Teenager"
# 20–59 → "Adult"
# 60+ → "Senior Citizen"
def age_group(age):
    if age<=13:
        print('child')
    elif 13<age<=19:
        print('teenager')
    elif 19<age<=59:
        print('adult')
    else:
        print('Senior citizen')
age_group(44)

# def age_group(age):
#     if age<=13:
#         return 'child'
#     elif 13<age<=19:
#         return 'teenager'
#     elif 19<age<=59:
#         return 'adult'
#     else:
#         return 'Senior citizen'
# print(age_group(23))