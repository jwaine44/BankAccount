class BankAccount:
    bank_name = "First National Bank"
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance:", str("$" + str(self.balance)))

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Your balance is zero!")
        return self

    @classmethod
    def all_balances(cls):
        for account in cls.all_accounts:
            print("Balance:", str("$" + str(account.balance)))

account1 = BankAccount(.01, 1000)

# Make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line
account1.deposit(100).deposit(200).deposit(700).withdraw(1000).yield_interest().display_account_info()

account2 = BankAccount(.05, 10000)

# Make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line
account2.deposit(150).deposit(550).withdraw(1300).withdraw(2400).withdraw(50).withdraw(1950).yield_interest().display_account_info()

BankAccount.all_balances()