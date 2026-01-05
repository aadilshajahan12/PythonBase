# Question: Use filter() and lambda to remove empty or blank-only strings.
# Example data:
#
# lines = ["data", "", " ", "ai", "  ", "ml"]
# # Expected → ['data', 'ai', 'ml']
#
lines = ["data", "", " ", "ai", "  ", "ml"]
f=list(filter(lambda x:x.strip(),lines))
print(f)