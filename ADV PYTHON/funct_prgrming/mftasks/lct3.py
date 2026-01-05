string="Python makes it easy to write powerful and readable code quickly"
#
# 5. Count number of spaces in a string
#
# 6. Find total number of vowels in a string
#
# 7. Find all of the words in a string that are less than 4 letters
print(string.count(" "))
print([string.count(i) for i in set(string) if i==' '])
print([(i,string.count(i)) for i in set(string) if i in 'aeiouAEIOU'])
print([i for i in string.split() if len(i)<4])
