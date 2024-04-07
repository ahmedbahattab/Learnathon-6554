class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)


# Example usage:
student1 = Student("John", 20)
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

print(f"Average grade for {student1.name}: {student1.get_average_grade()}")
