# Create a Python class called Student with attributes name, age, and grades, and methods to add grades, calculate average grade, and display student information.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Grades:", self.grades)
        print("Average Grade:", self.calculate_average_grade())

# Example usage:
# Create a Student object
student = Student("John", 20)

# Add grades
student.add_grade(90)
student.add_grade(85)
student.add_grade(95)

# Display student information
student.display_info()
