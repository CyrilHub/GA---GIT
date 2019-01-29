# Bank accounts keep track of their current balance
class BankAccount:
    
    def __init__(self, act_balance=0):
        self.act_balance = act_balance
     
    
    # Return False if someone tries to deposit or withdraw a negative amount.
    def positive_input_checker(self, deposite_amount=0, withdraw_amount=0):
        if deposite_amount > 0 or withdraw_amount > 0:
            pass
        else:
            print ("You have entered a negative value. Please be sure to in enter a positive value")
            return False
   
    #  Increase Acccount Balance by 2%
    def accumulate_interest(self, balance_change = 0):
        interest_rate = 0.02
        self.act_balance += balance_change * interest_rate    
        return self.act_balance
          
    # Deposit method returns the balance of the account after adding the deposited amount
    def deposit(self, deposit_amount):
        
        # Checks if input is positive
        if self.positive_input_checker(deposit_amount) == False:
            return False
        
        # Adds deposite to account balance
        self.act_balance += deposit_amount

        # Adds interestes rate
        self.accumulate_interest(self.act_balance)
        print ("Deposit - Amount:", deposit_amount)
        print ("Deposit - Basic account has:", self.act_balance)
        return self.act_balance
   
    # Withdraw method returns the amount of money that was successfully withdrawn
    def withdraw(self, withdraw_amount):
        # Checks if input is positive
        if self.positive_input_checker(withdraw_amount) == False:
             return False
        # Substract deposite to account balance
        self.act_balance -= withdraw_amount
        print ("Withdraw - Amount:", withdraw_amount)
        print ("Withdraw - Basic account has:", self.act_balance)
        return withdraw_amount
    

class ChildrensAccount(BankAccount):
    def __init__(self): 
        super().__init__() 
        self.interest_rate = 0
    
    # def accumulate_interest(self):
    #     # Every time accumulate_interest is executed on a Child's account 
    #     # the account always gets $10 added to the balance
    #     self.act_balance += 10  
    #     return self.act_balance
         
    

    
        # ================================================  #

basic_account = BankAccount(100)
basic_account.deposit(600)
basic_account.withdraw(17)

# basic account ftr
    # print("Basic account has ${}".format(basic_account.balance))
    # 
    # print("Basic account has ${}".format(basic_account.balance))
    # basic_account.accumulate_interest()
    # print("Basic account has ${}".format(basic_account.balance))
    # print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
# Children account test
    # print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
    # print("Child's account has ${}".format(childs_account.balance))
    # childs_account.accumulate_interest()
    # print("Child's account has ${}".format(childs_account.balance))
