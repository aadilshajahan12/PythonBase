# Filter strings starting with a vowel
#
# Question: Filter out only the names that start with a vowel using filter() and lambda.
# Example data:
#
# fruits = ["Apple", "Mango", "Orange", "Pineapple", "Avocado"]
# # Expected → ['Apple', 'Orange', 'Avocado']
#
#
fruits = ["Apple", "Mango", "Orange", "Pineapple", "Avocado"]
f=list(filter(lambda x:x[0] in 'AEIOU',fruits))
print(f)