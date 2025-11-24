# 6.Area Calculator

# Define area(shape, value1, value2)
# If shape == 'circle' → area
# If shape == 'rectangle' → area
# If shape == 'square' → area

# def area(shape,val1,val2=0):
#     if shape=='circle':
#         print('area=',3.14*val1**2)
#     elif shape=='rectangle':
#         print('area=', val1*val2)
#     else:
#         print('area=',val1**2)
# area('circle',4)

def area(shape,val1,val2=0):
    if shape=='circle':
        return 3.14*val1**2
    elif shape=='rectangle':
        return val1*val2
    else:
        return val1**2
print('area',area('square',10))