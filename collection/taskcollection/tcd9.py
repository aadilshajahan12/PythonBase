# 9. Create a nested dictionary for two students with keys: name, marks, and pass/fail
students = {
    "stu1": {"name": "Asha", "marks": 78, "status": "Pass"},
    "stu2": {"name": "Manu", "marks": 45, "status": "Fail"}
}
# Task: Print the marks of Manu
print(students['stu2']['marks'])
