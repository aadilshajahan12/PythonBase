# 14. Abbreviate college names
#
# Question: Convert full college names into uppercase abbreviations using the first letter of each word.
#
# Example data:
#
# colleges = ["National Institute of Technology",
#             "Indian Institute of Science",
#             "College of Engineering Trivandrum",
#             "Government Engineering College Palakkad"]
#
# # Expected → ['NIT', 'IIS', 'CET', 'GECP']
colleges = ["National Institute of Technology",
            "Indian Institute of Science",
            "College of Engineering Trivandrum",
            "Government Engineering College Palakkad"]
f=list(map(lambda x:''.join(c for c in x if c.isupper()),colleges))
print(f)