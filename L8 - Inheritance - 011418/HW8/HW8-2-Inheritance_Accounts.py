#Bank accounts keep track of their current balance
class BankAccount:
    def __init__(self, act_balance=0):
        self.act_balance = act_balance

    def positive_input_checker(self, deposite_amount=0, withdraw_amount=0):
        if deposite_amount > 0 or withdraw_amount > 0:
            pass
        else:
            return False
    
          
    #deposit method returns the balance of the account after adding the deposited amount
    def deposit(self, deposit_amount):
        if positive_input_checker(deposit_amount) == False:
            return False
        self.act_balance += deposit_amount
        print ("Deposit - Basic account has:", self.act_balance)
        return self.act_balance
    #withdraw method returns the amount of money that was successfully withdrawn
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

