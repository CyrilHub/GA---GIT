class BankAccount():

  def __init__(self, current_balance=0):
    self.current_balance=current_balance
    self.interest_rate=0.02
    print("A new bank account has been created with a 2 percent interest rate. You current balance is ${}".format(self.current_balance))
    

  def deposit(self, deposit):
    if deposit < 0:
      print("False. You cannot deposit a negative amount")
    else:
      self.current_balance += deposit
      print("Your deposit of {} is complete. Your current balance is {}".format(deposit, self.current_balance))
  

  def withdraw(self, withdraw):
    if withdraw < 0:
        print("False. You cannot withdraw a negative amount.")
    else:
        self.current_balance -= withdraw
        print("Your withdrawl of {} is complete. Your current balance is {}".format(withdraw, self.current_balance))
        return(self.current_balance)

  def accumulate_interest(self, accumulate_interest):
    print("The interest accumulated on your account is ${}".format(self.current_balance*self.interest_rate))
    self.current_balance *= 1+accumulate_interest
    return(self.current_balance)

class ChildrensAccount(BankAccount):

  def __init__(self, current_balance):
    self.current_balance=current_balance
    self.interest_rate = 0.00
    print("Your children's account has been created, The current balance is ${}.". format(self.current_balance))

  def accumulate_interest(self):
    new_interest_amount = 10
    self.current_balance +=new_interest_amount
    print("Your children's account now has an additional {} in interest. You current balance is {}".format(new_interest_amount, self.current_balance))

class OverdraftAccount(BankAccount):

  def __init__(self, current_balance):
    self.current_balance = current_balance
    self.interest_rate = 0.02
    self.overdraft = 40
    print("Your overdraft account has been created. The current balance is ${}".format(self.current_balance))

    def withdraw(self, withdraw):
      if withdraw > self.current_balance:
        print("False. The amount you attempted to withdraw, ${}, is greater than your current balance of ${}.".format(withdraw, self.current_balance))
        self.current_balance -= overdraft
        print("Your account balance has been reduced by ${} and your current balance is now ${}".format(self.overdraft, self.current_balance))
        return self.current_balance
      else:
        super().withdraw(withdraw)

    def accumulate_interest(self):
        if self.current_balance < 0:
            print("This account has been overdrawn and cannot accumulate interest.")
        else:
            super().accumulate_interest()




basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.current_balance))
basic_account.withdraw(17)
print("Basic account has ${}".format(basic_account.current_balance))
basic_account.accumulate_interest(0.02)
print("Basic account has ${}".format(basic_account.current_balance))
childs_account = ChildrensAccount(0)
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.current_balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.current_balance))
childs_account.accumulate_interest()
print("Child's account has ${}".format(childs_account.current_balance))
overdraft_account = OverdraftAccount(0)
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.current_balance))
overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.current_balance))
# overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.current_balance))
    