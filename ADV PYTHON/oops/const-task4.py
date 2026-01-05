# Create a class *Employee* with:
#
# * name
# * salary
#
# Initialize them using a constructor.
# Add a method to increase the salary by *10%* and show the new salary.
#
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def inc(self):
        self.salary*=1.1
        print('new salary: ',int(self.salary))
s=Employee('anand',100)
s.inc()