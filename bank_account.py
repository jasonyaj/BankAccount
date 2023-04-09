class BankAccount:
    bank_name = 'First National Dojo'
    members_list = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.members_list.append(self)

    # Methods
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance - 5
            print('Insufficient funds: Charging a $5 fee')
        return self

    def display_account_info(self):
        balance = self.balance
        print('Balance:', balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1 + self.int_rate)
        return self

    @classmethod
    def print_all_instances( cls ):
        for members in cls.members_list:
            members.display_account_info()


jason = BankAccount(0.01, 100)
debbie = BankAccount(0.01, 500)

jason.deposit(50).deposit(75).deposit(25).withdraw(20).yield_interest()
debbie.deposit(50).deposit(70).withdraw(20).withdraw(40).withdraw(40).withdraw(800).yield_interest()

BankAccount.print_all_instances()