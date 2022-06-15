class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= amount + 5
            return self
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        return f"Balance: {self.balance}"

    def yield_interest(self):
        self.balance = self.balance - (self.balance * self.int_rate)
        return self

    @classmethod
    def get_all_instances(cls):
        counter = 1
        account_list = "-"*50+"\n"
        for account in cls.all_accounts:
            account_list += f"account {counter}\n"
            account_list += f"  Interest Rate: {account.int_rate}\n  Balance: {account.balance}\n"
            counter += 1
            account_list += "-"*50+"\n"*2
        return account_list

account_1 = BankAccount(0.1, 0)
account_2 = BankAccount(0.15, 0)
account_3 = BankAccount(0.12, 0)

print(BankAccount.get_all_instances())
print("A"*50)
print(account_1.deposit(50).deposit(100).deposit(85).withdraw(200).yield_interest().display_account_info())

print(account_2.deposit(100).deposit(150).withdraw(50).withdraw(100).withdraw(50).withdraw(55).yield_interest().display_account_info())

print(account_3.deposit(200).deposit(130).withdraw(50).withdraw(130).withdraw(50).withdraw(30).yield_interest().display_account_info())

print("B"*50)
print(BankAccount.get_all_instances())

