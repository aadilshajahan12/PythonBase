# Create a class *Product* with constructor parameters:
#
# * name
# * price
#
# Add a method to apply *5% discount* and show the new price.
class Product:
    def __init__(self,name,price):
        self.price=price
    def newp(self):
        print('new price: ',self.price*.95)
p=Product('donny',100)
p.newp()