
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {"checking": BankAccount(0.02, 0),"savings": BankAccount(0.05, 600)}

    def make_deposit(self,account_name,amount):
        self.account[account_name].deposit(amount)
        return self

    def make_withdrawl(self,account_name,amount):
        self.account[account_name].withdraw(amount)
        return self

    def display_user_balance(self,account_name):
        print(f"{self.name}'s Current {account_name} Balance is: {self.account[account_name].balance}")
        return self

    def transfer_money(self,amount,other_user,account_name):
        self.account[account_name].balance -= amount
        other_user.account[account_name].balance += amount
        print(f"You transferred {amount} to {other_user.name}!")
        return self


# account_1 = BankAccount(0.1, 0)
# account_2 = BankAccount(0.15, 0)
# account_3 = BankAccount(0.12, 0)

person_1 = User("Jerry", "jerry@email.com")
person_2 = User("Alex", "alex@email.com")

# print("A"*50)

# print(account_1.deposit(50).deposit(100).deposit(85).withdraw(200).yield_interest().display_account_info())

# print(account_2.deposit(100).deposit(150).withdraw(50).withdraw(100).withdraw(50).withdraw(55).yield_interest().display_account_info())

# print(account_3.deposit(200).deposit(130).withdraw(50).withdraw(130).withdraw(50).withdraw(30).yield_interest().display_account_info())

# print("B"*50)

# print(BankAccount.get_all_instances())

# print("C"*50)

person_1.make_deposit("checking",500).display_user_balance("savings")
print("A"*50)
person_1.make_deposit("checking",500).make_deposit("savings",500).display_user_balance("savings").display_user_balance("checking")
print("B"*50)
person_1.transfer_money(50,person_2,"checking")
person_2.display_user_balance("checking")



