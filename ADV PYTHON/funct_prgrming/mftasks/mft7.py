# 9. From ["apple", "an", "cat", "ok"], filter only the words with length greater than 3 using filter and a lambda. and a lambda.
l=["apple", "an", "cat", "ok"]
f=list(filter(lambda x:len(x)>3,l))
print(f)