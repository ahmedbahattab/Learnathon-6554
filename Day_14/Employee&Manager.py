class Employee:
    def __init__(self, name, salary, bonus_percentage):
        self.name = name
        self.salary = salary
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self):
        return self.salary * (self.bonus_percentage / 100)


class Manager(Employee):
    def __init__(self, name, salary, bonus_percentage, department):
        super().__init__(name, salary, bonus_percentage)
        self.department = department

    def calculate_bonus(self):
        # Override the calculate_bonus method to include a bonus of 10% of the salary for managers
        base_bonus = super().calculate_bonus()
        manager_bonus = self.salary * 0.10
        return base_bonus + manager_bonus


# Create instances of Employee and Manager classes
employee1 = Employee("John Doe", 50000, 5)
manager1 = Manager("Jane Smith", 80000, 8, "Marketing")
manager2 = Manager("Alice Johnson", 75000, 6, "Finance")

# Print out the bonus amount for each employee
print("Employee 1 bonus:", employee1.calculate_bonus())
print("Manager 1 bonus:", manager1.calculate_bonus())
print("Manager 2 bonus:", manager2.calculate_bonus())
