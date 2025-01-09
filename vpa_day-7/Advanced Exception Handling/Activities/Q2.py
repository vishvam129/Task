# Create a custom exception class InsufficientBalanceError for a banking program.

class InsufficientBalanceError(Exception):
    def __init__(self, message = "Your balance is Insufficient "):
        super().__init__(message)
    
class Bank:
    def __init__(self,acno,balance):
        self.acno = acno
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientBalanceError()
        else:
            self.balance -= amount

person = Bank(123,45000)
person.withdraw(89000)