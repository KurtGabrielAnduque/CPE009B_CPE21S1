import Accounts
import ATM

Account1 = Accounts.Accounts(account_number=123456,account_firstname = "Kurt Gabriel",account_lastname = "Anduque",current_balance = 1000,address = "Morato Quezon city", email = "anduquekurt@gmail.com")

print("================Account1================")


Account1.Account_check()


user1_serialnumber = 12345
ATM1 = ATM.ATM(user1_serialnumber,500,"deposit")
ATM1.deposit(Account1)
ATM1.check_currentbalance(Account1)
ATM1.check_serialnumber()
ATM1.view_transactionsummary()

print('\n')
print("================Account2================")

Account2 = Accounts.Accounts(account_number=321349, account_firstname = "Marc Karol",account_lastname = "Badar",current_balance = 2000,address = "Morato Quezon City",email = "tardypancake@gmail.com")

Account2.Account_check()

user2_serialnumber = 67891
ATM2 = ATM.ATM(user2_serialnumber,300,"deposit")
ATM2.deposit(Account2)
ATM2.check_currentbalance(Account2)
ATM2.check_serialnumber()
ATM2.view_transactionsummary()
