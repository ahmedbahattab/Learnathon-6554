'''> Create a function called **`grade_converter`** that takes a numerical grade as an argument and returns the corresponding letter grade (A, B, C, D, F) based on the standard grading scale.
> 
- If the score is greater than or equal to 90, print "A"
- If the score is between 80 and 89, print "B"
- If the score is between 70 and 79, print "C"
- If the score is between 50 and 69, print "D"
- If the score is below 50, print "F" '''
def grade_converter(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 50 <= score < 70:
        return "D"
    else:
        return "F"
numerical_grade = float(input("Enter the numerical grade: "))
letter_grade = grade_converter(numerical_grade)
print(f"The corresponding letter grade is: {letter_grade}")
