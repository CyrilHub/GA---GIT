# Bank accounts keep track of their current balance
class BankAccount:
    
    def __init__(self, balance=0):
        self.balance = balance
     
    # Return False if someone tries to deposit or withdraw a negative amount.
    def positive_input_checker(self, deposite_amount=0, withdraw_amount=0):
        if deposite_amount > 0 or withdraw_amount > 0:
            pass
        else:
            print ("You have entered a negative value. Please be sure to in enter a positive value")
            return False
   
    #  Increase Acccount Balance by 2%
    def accumulate_interest(self):
        interest_rate = 0.02
        self.balance += self.balance * interest_rate

        return self.balance

# ===============================================================================  #


    # Deposit method returns the balance of the account after adding the deposited amount
    def deposit(self, deposit_amount):
        
        # Checks if input is positive
        if self.positive_input_checker(deposit_amount) == False:
            return False
        
        # Adds deposite to account balance
        self.balance += deposit_amount
        return self.balance
   

    # Withdraw method returns the amount of money that was successfully withdrawn
    def withdraw(self, withdraw_amount):
       
        # Checks if input is positive
        if self.positive_input_checker(withdraw_amount) == False:
            return False
       
        # Substract deposite to account balance
        self.balance -= withdraw_amount

        # Notify user that withdraw was processed
        return withdraw_amount


class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.overdraft_penalty = 40

    
    #  Increase Acccount Balance by 2%
    def accumulate_interest(self):
        interest_rate = 10
        self.balance = self.balance + interest_rate

        return self.balance
    # def accumulate_interest(self):
    #     # Every time accumulate_interest is executed on a Child's account 
    #     # the account always gets $10 added to the balance
    #     self.balance += 10  
    #     return self.balance
         
class  OverdraftAccount(BankAccount):
    def __init__(self):
        super().__init__() 
        self.overdraft_penalty = 40
    
    # Withdraw method returns the amount of money that was successfully withdrawn
    def withdraw(self, withdraw_amount):
       
        # Checks if input is positive
        if self.positive_input_checker(withdraw_amount) == False:
            return False
        
        elif withdraw_amount > self.balance:
            self.balance -= self.overdraft_penalty
            return False
       
        else:
            # Substract deposite to account balance
            self.balance -= withdraw_amount

            # Notify user that withdraw was processed
            return withdraw_amount

    #  Increase Acccount Balance by 2% for Overdraft account
    def accumulate_interest(self):
        interest_rate = 0.02
        
        if self.balance < 0:
            return self.balance
        
        else:
            self.balance += self.balance * interest_rate
            return self.balance


basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${}".format(overdraft_account.balance))