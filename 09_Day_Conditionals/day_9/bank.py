from unicodedata import name


# class Account:
#     def __init__(self,bank_name,acc_number,balance,password):
#         self.bank_name=bank_name
#         self.acc_number=acc_number
#         self.balance=balance
#         self.password=password

#     def deposit(self):
#         dep_amount=int(input('Enter amount you want to deposit : '))
#         dep_amount+=self.balance
#         return f'Your new balance is {dep_amount}'

#     def withdraw(self):
#         wthdr_amount = int(input('Enter amount you want to withdraw : '))
#         self.balance-=wthdr_amount
#         return f'Your new balance is{self.balance}'
class Account:
    def __init__ (self,name,number):
        self.name=name
        self.number=number
        self.balance= 0
        self.deposits=[]
        self.withdrawals=[]


    def deposit(self,amount):
        if amount<=0:
            return f"deposit amount must be greater than zero"
        else:
         self.balance+=amount
         self.deposits.append(amount)
        return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance} and your successful deposit amount is {self.deposits}"


# acc1=Account(name="Effence",number=123)
# acc2=Account(name="Susan",number=123)
# acc1.deposit(1000)
# print(acc1.deposit(10000))
# print(acc2.deposit(7000))
# print(acc2.deposit(7000))
# print(acc1.deposit(-5000))
    
    def withdraw(self,amount):
        if amount> self.balance:
            return f"Insufficient funds"
        elif amount<=0:
            return f"Amount must be greater than zero"
        else:
            self.withdrawals.append(amount)
            self.transaction_cost=100
            self.balance-=amount + self.transaction_cost
            return f"Hello {self.name} you have withdrawn {amount} your new balance is {self.balance} and successful withdrawal amount is{self.withdrawals}"

    def deposits_statement(self):
        for depos in self.deposits:
            return f"Your have deposited \n {depos}"

    def withdrawals_statement (self):
        for withdrawn in self.withdrawals:
            return f"You have withdrawn \n {withdrawn}"
    def balance(self):
        return f"Your balance is {self.balance}"
# >>> from bank import Account
# acc1=Account(name="Cudra",number=123456)
# acc2=Account(name="Nash",number=345678)
# print(acc1.deposit(90000))
# print(acc1.withdrawal(900000))
# print(acc1.withdrawal(-900000))
# print(acc1.withdrawal(9000))

# print(acc2.deposit(200000))
# print(acc2.withdrawal(-200000))
# print(acc2.withdrawal(20000000))
# print(acc2.withdrawal(2000))

#Add a new attribute to the class Account called deposits which by default is an empty list.
# Add another attribute to the class Account called withdrawals which by default is an empty list.
# Modify the deposit method to append each successful deposit to self.deposits
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
# Add a new method called deposits_statement which using a for loop prints each deposit in a new line
# Add a new method called withdrawals_statement which using a for loop prints each withdrawal in a new line

# Modify the withdrawal method to include a transaction fee of 100 per transaction.
# Add a method to show the current balance