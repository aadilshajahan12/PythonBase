# Question: Use map() and lambda to extract only the domain name from a list of email addresses.
# Example data:
#
# emails = ["joseph@outlook.com", "anita@gmail.com", "sunil@yahoo.com"]
# # Expected → ['outlook.com', 'gmail.com', 'yahoo.com']
#
#
emails = ["joseph@outlook.com", "anita@gmail.com", "sunil@yahoo.com"]
f=list(map(lambda x:x.split('@'),emails))
f1=list(map(lambda x:x[1],f))
print(f1)