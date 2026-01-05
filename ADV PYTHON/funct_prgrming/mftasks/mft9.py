# Create email addresses from names
#
# Question: Use map() and lambda to convert a list of full names into lowercase Gmail addresses (firstname + lastname@gmail.com).
# Example data:
#
# names = ["Arjun Das", "Meera K Nair", "Vishnu R"]
# # Expected → ['arjundas@gmail.com', 'meeraknair@gmail.com', 'vishnur@gmail.com']
#
names = ["Arjun Das", "Meera K Nair", "Vishnu R"]
f=list(map(lambda x:''.join(x.lower().split()),names))
f2=list(map(lambda x:x+"@gmail.com",f))

print(f2)
