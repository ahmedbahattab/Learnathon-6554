"""
Create a program that takes a student's exam score as input. Classify the student's performance as follows:
- If the score is greater than or equal to 90, print "A"
- If the score is between 80 and 89, print "B"
- If the score is between 70 and 79, print "C"
- If the score is between 50 and 69, print "D"
- If the score is below 50, print "F"
"""

exam_score = float(input("Enter the student's exam score: "))

if exam_score >= 90:
    grade = "A"
elif 80 <= exam_score <= 89:
    grade = "B"
elif 70 <= exam_score <= 79:
    grade = "C"
elif 50 <= exam_score <= 69:
    grade = "D"
else:
    grade = "F"

print("Student's performance: Grade", grade)
