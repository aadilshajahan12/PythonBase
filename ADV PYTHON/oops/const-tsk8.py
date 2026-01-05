# Create a class *StudentMarks* whose constructor accepts:
#
# * mark1
# * mark2
# * mark3
#
# Add a method to calculate the percentage using:
#
# Percentage = (total / 300) × 100
#
class StudentMArks:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def cal(self):
        return (self.m1+self.m2+self.m3)/3
s=StudentMArks(66,77,88)
print(s.cal())