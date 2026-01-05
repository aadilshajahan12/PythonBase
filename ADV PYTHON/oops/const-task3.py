# Create a class *BankAccount* whose constructor accepts:
#
# * account number
# * account holder name
# * balance
#
# Add a method to display all the account details neatly.
class BankAccount:
    def __init__(self,accno,accname,bal):
        self.accno=accno
        self.accname=accname
        self.bal=bal

    def view(self):
        print(' Account no:',self.accno,'\n Account name',self.accname,'\n Bal',self.bal)
b=BankAccount(390522,'abhilash',10000)
b.view()

