# Create a class *EmployeeExperience* with constructor values:
#
# * employee name
# * joining year
# * current year
#
# Add a method to calculate the number of years of experience.
class EmployeeExperience:
    def __init__(self,empname,joiny,cy):
        self.empname=empname
        self.joiny=joiny
        self.cy=cy
    def exp(self):
        return self.cy-self.joiny
e=EmployeeExperience('nani',2020,2025)
print('experience:',e.exp())
