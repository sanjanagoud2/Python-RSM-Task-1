class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful", self.balance)
        else:
            print("Insufficient funds")

class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest_earned = self.balance * self.interest_rate
        self.deposit(interest_earned)
        print("Interest earned:", interest_earned)

class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def apply_overdraft(self, amount):
        if self.balance + self.overdraft_limit >= amount:
            self.balance -= amount
            print("Overdraft applied", self.balance)
        else:
            print("Overdraft limit exceeded")
johnSavings = SavingsAccount("111111", 2000, 1.5)
janeChecking = CheckingAccount("22222", 1000, 500)
johnSavings.deposit(200)
johnSavings.withdraw(300)
janeChecking.deposit(100)
janeChecking.withdraw(1500)
janeChecking.apply_overdraft(2000)