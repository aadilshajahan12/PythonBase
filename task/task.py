# Write a python program that takes a sentence and returns a dictionary where:
# Keys are words in the sentence.
# Values are dictionaries with:
# “length”->Length of the word
# “is_palindrome”->True if the word is palindrome,otherwise False.
# “count” ->number of occurences of the word
#
# Sample Input:
# Sentence=”madam and racecar are level racecar madam”

l=input('enter the text')
l=l.split()
# for i in l:
#     l2={}
#     l2['length']=len(i)
#     l2['is_palindrome']= i==i[-1::-1]
#     l2['count']=l.count(i)
#     l1[i]=l2
# print(l1)

l1=