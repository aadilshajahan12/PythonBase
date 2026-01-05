# Question: Use filter() and lambda to return only the palindrome words from the list.
# Example data:
#
# words = ["malayalam", "hello", "level", "world", "noon"]
# # Expected → ['malayalam', 'level', 'noon']
words = ["malayalam", "hello", "level", "world", "noon"]
f=list(filter(lambda x:x==x[::-1],words))
print(f)