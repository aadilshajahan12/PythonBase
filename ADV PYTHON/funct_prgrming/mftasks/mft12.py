# Question: Use map() and lambda to capitalize full names correctly (title case).
# Example data:
#
# names = ["rahul r", "deepa menon", "vivek raj"]
# # Expected → ['Rahul R', 'Deepa Menon', 'Vivek Raj']
#
#
names = ["rahul r", "deepa menon", "vivek raj"]
f=list(map(lambda a:a.title(),names))
print(f)