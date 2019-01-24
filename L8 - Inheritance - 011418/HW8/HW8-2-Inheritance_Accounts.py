# Bank accounts keep track of their current balance
class BankAccount:

    def __init__(self, act_balance=0):
        self.act_balance = act_balance
        self.interest_rate = 0.2

    
    # Return False if someone tries to deposit or withdraw a negative amount.
    def positive_input_checker(self, deposite_amount=0, withdraw_amount=0):
        if deposite_amount > 0 or withdraw_amount > 0:
            pass
        else:
            return False
   
    #  Increase Acccount Balance by 2%
    def accumulate_interest(self):
        self.act_balance += act_balance * interest_rate    
        return self.act_balance
          
    # Deposit method returns the balance of the account after adding the deposited amount
    def deposit(self, deposit_amount):
        # Checks if input is positive
        if self.positive_input_checker(deposit_amount) == False:
            return False
        # Adds deposite to account balance
        self.act_balance += deposit_amount
        # Update act_balance at class level
        # ??? why can't i assign it to act_balance direct
        act_balance_class = self.act_balance
        # Adds interestes rate
        self.accumulate_interest(act_balance_class)
        print ("Deposit - Amount:", deposit_amount)
        print ("Deposit - Basic account has:", act_balance_class)
        return act_balance_class
   
    # Withdraw method returns the amount of money that was successfully withdrawn
    def withdraw(self, withdraw_amount):
        # Checks if input is positive
        if self.positive_input_checker(withdraw_amount) == False:
             return False
        # Substract deposite to account balance
        self.act_balance -= withdraw_amount
        # Update act_balance at class level
        act_balance_class = self.act_balance
         # Adds interestes rate
        self.accumulate_interest(deposit_amount)
        # ================================================  #
        print ("Withdraw - Amount:", withdraw_amount)
        self.accumulate_interest(deposit_amount, withdraw_amount)
        print ("Withdraw - Basic account has:", act_balance_class)
        return withdraw_amount
    
 

basic_account = BankAccount(100)
basic_account.deposit(600)
basic_account.withdraw(17)


# print("Basic account has ${}".format(basic_account.balance))
# 
# print("Basic account has ${}".format(basic_account.balance))
# basic_account.accumulate_interest()
# print("Basic account has ${}".format(basic_account.balance))
# print()

