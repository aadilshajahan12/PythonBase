# Question: Use map() and lambda to clean up strings by removing special characters (only alphabets and numbers).
# Example data:
#
# texts = ["he@llo!", "w#orld$", "^python^3"]
# # Expected → ['hello', 'world', 'python3']
#
texts = ["he@llo!", "w#orld$", "^python^3"]
f=list(map(lambda x:''.join(c for c in x if c.isalnum()),texts))
print(f)