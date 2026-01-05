# Create a class *Student* with a constructor that takes:
#
# * student name
# * age
#
# Create an object and print the name and age using the object.
#
# ---
class Student:
    def __init__(self,stname,age):
         print(stname,age)
s=Student('john',21)