# Question: Use map() and lambda to return the length of each string in a list.
# Example data:
#
# words = ["machine", "learning", "ai", "model"]
# # Expected → [7, 8, 2, 5]
words = ["machine", "learning", "ai", "model"]
f=list(map(lambda x:len(x),words))
print(f)