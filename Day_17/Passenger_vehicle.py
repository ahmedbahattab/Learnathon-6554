class Vehicle:
    def drive(self):
        print("Vehicle is being driven.")

class Passenger:
    def carry_passengers(self):
        print("Passengers are being carried.")

class Car(Vehicle, Passenger):
    def drive_and_carry(self):
        self.drive()  # Call drive() method from Vehicle class
        self.carry_passengers()  # Call carry_passengers() method from Passenger class

# Creating an instance of Car
my_car = Car()

# Calling the drive_and_carry() method
my_car.drive_and_carry()
