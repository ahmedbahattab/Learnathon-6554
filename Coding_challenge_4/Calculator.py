class Calculator:
    def __init__(self):
        self.__result = 0  # Initialize the private attribute

    def add(self, num):
        self.__result += num

    def subtract(self, num):
        self.__result -= num

    def multiply(self, num):
        self.__result *= num

    def divide(self, num):
        if num != 0:
            self.__result /= num
        else:
            print("Error: Division by zero")

    def get_result(self):
        return self.__result


# Example usage:
calc = Calculator()
calc.add(5)
calc.subtract(3)
calc.multiply(2)
calc.divide(4)
print("Result:", calc.get_result())  # Output should be 2.0
