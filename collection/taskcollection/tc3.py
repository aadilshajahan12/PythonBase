# find
# the
# longest
# occurring
# word in the
# list
# lst = ['apple', 'orange', 'apple', 'grapes', 'apple', 'bananna'] - -- o / p
# will
# be
# apple(repeated
# the
# most)
#
lst = ['apple', 'orange', 'apple', 'grapes', 'apple', 'bananna']
s=0
a=''
for i in lst:
    if lst.count(i)>s:
        s=lst.count(i)
        a=i
print(a)