# .Fruit Price Checker

# Define fruit_price(fruit)
# If 'apple' → price of apple is 120 Rs per kg
# If 'banana' → 50/kg
# If 'mango' → 120/kg
# Else → "Not available"

# def fruit_price(fruit):
#     if fruit=='apple':
#         print('price=120')
#     elif fruit=='banana':
#         print('price=50')
#     elif fruit=='mango':
#         print('price=120')
#     else:
#         print('not available')
# fruit_price('banana')

def fruit_price(fruit):
    if fruit=='apple':
        return 'price=120'
    elif fruit=='banana':
        return'price=50'
    elif fruit=='mango':
        return'price=120'
    else:
        return'not available'
print(fruit_price('mango'))