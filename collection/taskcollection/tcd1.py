# Count how many times each word appears in the sentence
# sentence = "Python is simple yet powerful and Python is popular"
# Task: Store each word and its count in a dictionary
s="Python is simple yet powerful and Python is popular"
s=s.split()
l=set(s)
d={}
for i in l:
   d[i]=s.count(i)
print(d)