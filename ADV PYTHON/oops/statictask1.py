# create a class  name Employee
# details -- id , fname , lname , age , prof , loc, company_name  (same company)
# 5 objects

class Employee:
    compname='HCL'
    def details(self,id,fname,lname,age,prof,loc):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.loc=loc

    def view(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.loc,Employee.compname)

obj1=Employee()
obj1.details(101,'arham','junaijo',22,'chitchat','aluva')
obj1.view()
obj2=Employee()
obj2.details(102,'arun','smokie',29,'vlogger','aluva')
obj2.view()
obj3=Employee()
obj3.details(103,'azeez','ma',85,'chef','ekm')
obj3.view()
obj4=Employee()
obj4.details(104,'shqjji','karunakar',65,'director','kolam')
obj4.view()
obj5=Employee()
obj5.details(105,'shibu','p',34,'job','pattambi')
obj5.view()