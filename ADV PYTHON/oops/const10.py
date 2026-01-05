# Create a class *Book* with constructor values:
#
# * title
# * author
# * price
#
# Add a method to display all book details.
#
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def priint(self):
        print(self.title,'\n',self.author,'\n',self.price)
b=Book('war and love','leo tolstoy',899)
b.priint()