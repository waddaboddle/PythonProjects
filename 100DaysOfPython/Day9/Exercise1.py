student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if 91 <= student_scores[key] < 100:
        student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] < 90:
        student_grades[key] = "Exceeds Expectations"
    elif 71 <= student_scores[key] < 80:
        student_grades[key] = "Acceptable"
    elif 70 >= student_scores[key]:
        student_grades[key] = "Fail"

    # 🚨 Don't change the code below 👇
print(student_grades)
