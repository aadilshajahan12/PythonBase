# Create a class *Item* with constructor inputs:
#
# * item name
# * quantity
# * price per unit
#
# Add a method to calculate:
#
# Total bill = quantity × price per unit
class Item:
    def __init__(self,itemname,quantity,priceperunit):
        self.itemname=itemname
        self.quantity=quantity
        self.priceperunit=priceperunit
    def tot(self):
        return self.quantity*self.priceperunit
p=Item('shorts',10,130)
print(p.itemname,' Total bill:',p.tot())