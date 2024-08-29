class Account:
    def __init__(self, initial_balance=0):
        self.current_balance = initial_balance

class ATM:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.transactions = []

    def deposit(self, account, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        account.current_balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print("Deposit Complete")

    def withdraw(self, account, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > account.current_balance:
            print("Insufficient funds.")
            return
        account.current_balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        print("Withdrawal Complete")

    def check_current_balance(self, account):
        print(f"Current Balance: {account.current_balance}")
        
    def view_transactionsummary(self):
        for transactions in self.transactions:
            print(transactions)