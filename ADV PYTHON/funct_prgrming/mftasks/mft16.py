# Question: Add a # prefix to each word using map() and lambda.
# Example data:
#
# keywords = ["python", "datascience", "ai", "ml"]
# # Expected → ['#python', '#datascience', '#ai', '#ml']
#
keywords = ["python", "datascience", "ai", "ml"]
f=list(map(lambda x:'#'+x,keywords))
print(f)