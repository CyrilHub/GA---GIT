class BankAccount:
    def __init__(self, act_balance=0):
        self.act_balance = act_balance

    def positive_input(self, deposite_amount=0,withdraw_amount=0):
        if deposite_amount > 0:
            return True
        else:
            return False
    

            

    def deposit(self, deposit_amount):
        self.act_balance += deposit_amount
        print ("Deposit - Basic account has:", self.act_balance)
        return self.act_balance

    def withdraw(self, withdraw_amount):
        self.act_balance -= withdraw_amount
        print ("Withdraw - Amount:", withdraw_amount)
        print ("Withdraw - Basic account has:", self.act_balance)
        return withdraw_amount
    
    
    


basic_account = BankAccount()
basic_account.deposit(600)
basic_account.withdraw(17)


# print("Basic account has ${}".format(basic_account.balance))
# 
# print("Basic account has ${}".format(basic_account.balance))
# basic_account.accumulate_interest()
# print("Basic account has ${}".format(basic_account.balance))
# print()

