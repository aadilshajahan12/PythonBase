# Create a class *Circle*.
# The constructor should take *radius* as input.
# Add a method to calculate the *area* using:
#
# Area = 3.14 × radius × radius


class Circle:
    def __init__(self,rad):
        self.rad=rad
    def area(self):
        return 3.14*(self.rad**2)
r=Circle(10)
print('area =',r.area())