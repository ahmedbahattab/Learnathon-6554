class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")


class Professor(Person):
    def __init__(self, name, age, faculty_id):
        super().__init__(name, age)
        self.faculty_id = faculty_id

    def display_info(self):
        super().display_info()
        print(f"Faculty ID: {self.faculty_id}")


# Creating instances of Student and Professor
student = Student("Alice", 20, "S12345")
professor = Professor("Dr. Smith", 45, "F789")

# Demonstrate polymorphism by calling the display_info() method on each object
student.display_info()
print()  # Adding an empty line for clarity
professor.display_info()
