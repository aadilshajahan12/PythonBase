# 4. Find the length of each word in ["apple", "kiwi", "banana"] using map and a lambda
w=["apple", "kiwi", "banana"]
f=list(map(lambda x:len(x),w))
print(f)