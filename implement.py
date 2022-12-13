class Account:
    
    def __init__(self,title,balance):
        self.title = title
        self.balance = balance
        
    def display(self):
        return f"Name of Account Holder : {self.title} \nAcc Balance : {self.balance}"

class SavingsAccount(Account):

    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def display(self):
        data = super().display()
        return f"Name of Account Holder : {self.title} \nAcc Balance : {self.balance} \nInterest : {self.interestRate}"

obj = SavingsAccount("Arjun", 500, 5)
data = obj.display()
print("\nChallenge-4 Output:- \n", data)
