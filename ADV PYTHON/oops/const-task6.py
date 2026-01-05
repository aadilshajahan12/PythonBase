# Create a class *Temperature* whose constructor receives a value in *Celsius*.
# Add a method to convert it into *Fahrenheit* using:
#
# F = (C × 9/5) + 32
class Temperature:
    def __init__(self,cel):
        self.cel=cel
    def conv(self):
        f=(self.cel*9/5)+32
        return f
t=Temperature(100)
print(t.conv())