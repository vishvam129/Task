# Demonstrate encapsulation by creating private attributes (A/c No, 	balance) 
# for a BankAccount class and providing getter and setter methods.

class BankAccount:
    # def __init__(self,Acno,Balance):
    #     self.__Acno=Acno
    #     self.__Balance=Balance
    
    def get_info(self):
        return f"Your A/c No is {self.__Acno}  And your Balance is {self.__Balance}"
    
    def set_info(self,Acno,Balance):
        self.__Acno=Acno
        self.__Balance=Balance
    
Bank=BankAccount()
Bank.set_info(123,45000)
print(Bank.get_info())