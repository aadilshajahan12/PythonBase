# Create a class *Laptop* with constructor attributes:
#
# * brand
# * RAM
# * price
#
# # Create *three* laptop objects and print the details of each laptop.
class Laptop:
    def __init__(self,brand,ram,price):
        print('Brand:',brand, "ram:",ram,'price',price)
l1=Laptop('lenovo',13,12000)
l2=Laptop('dell',6,10000)
l3=Laptop('hp',7,15000)
