class BankAccount:
    def __init__(self, initial_balance, account_number):
        self.__balance = initial_balance
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            print("Deposit amount must be greater than zero.")
            return False

# Example usage
account = BankAccount(1000, "123456789")
print("Current balance:", account.get_balance())  # Output: Current balance: 1000
account.deposit(500)
print("After deposit:", account.get_balance())    # Output: After deposit: 1500
