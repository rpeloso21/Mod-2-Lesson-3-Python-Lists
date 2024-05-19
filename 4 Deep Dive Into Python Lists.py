# Task 1

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

subpar_index = []

for i in grades:
    if i < 80:
        subpar_index.append(grades.index(i))
        
for i in subpar_index:
    print(students[i], grades[i], activities[i])

# Task 2

students_approved = []

for student in students:
    for i in subpar_index:
        if students.index(student) != i:
            students_approved.append(student)

# Task 3

print(students_approved)