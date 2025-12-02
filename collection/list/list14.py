# You are given a list of integers, num_list, which represents a consecutive number series. In
# this list:
# There is one repeated number.
# There is one missing number.
# Your task is to write a Python function to:
# • Identify the repeated number.
# • Identify the missing number.
# • Calculate the sum of the repeated and missing numbers.
# Example 1:
# num_list = [1, 1, 3, 4]
# Output: 3 (Repeated number: 1, Missing number: 2, Sum: 1 + 2 = 3)
# Example 2:
# num_list = [1, 2, 2, 4]
# Output: 5 (Repeated number: 2, Missing number: 3, Sum: 2 + 3 = 5)
# Example 3:
# num_list = [2, 3, 3, 5]
# Output: 7 (Repeated number: 3, Missing number: 4, Sum: 3 + 4 = 7)
num_list = [1,2,3,3,5]
l=[]
for i in num_list:
   if i in l:
       print('repeated number ',i,'missing number',i+1,'sum=',i+(i+1))
   else:
       l.append(i)