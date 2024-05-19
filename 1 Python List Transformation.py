# Task 1

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()

print(grades)

# Task 2

total_of_grades = 0

for grade in grades:
    total_of_grades += grade

average_grade = total_of_grades / len(grades)

print(f"The average grade in the class is {average_grade}.")

# Task 3

index = 0

for grade in grades:
    if grade < 80:
        grades[index] = "Failed"

    index += 1

print(grades)
