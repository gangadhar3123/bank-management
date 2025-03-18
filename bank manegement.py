class account:
    def __init__(self,username,password,balance=0):
        self.username=username
        self.password=password
        self.balance=balance
class bankmanagement():
    def __init__(self):
        self.accounts={}
    def createaccount(self):
        username=input("Enter username:")
        password=input("Enter password:")
        if username in self.accounts:
            print("username already exists")
        else:
            self.accounts[username]=account(username,password,0)
            print("Account created successfully")
    def login(self):
        username=input("Enter your username:")
        password=input("Enter password:")
        if username in self.accounts:
            Account=self.accounts[username]
            if Account.password==password:
                print(f"Login successfull welcome,{username}")
                return Account
            else:
                print("Incorrect password:")
        else: 
            print("Username not found")
        return None
    def deposit(self,account):
        amount=float(input("Enter doposit amount:"))
        if amount>0:
            account.balance+=amount
            print(f"Deposited{amount} and balance:{account.balance}")
        else:
            print("Invalid amount")
    def withdraw(self,account):
        amount=float(input("Enter withdrawl amount:"))
        if amount<account.balance:
            account.balance-=amount
            print(f"withdraw{amount} and Balance:{account.balance}")
        else:
            print("Insufficient funds")
        def check_balance(self,account):
            print(f"Your current balance is:{account.balance}")
        def mini_statement(self,account):
            print("Mini statement:")
            print(f"username:{account.username}")
            print(f"Balance:{account.balance}")
        def exit(self):
            print("Thank you for using our ATM")
            exit()
bank=bankmanagement()
while True:
    print("*****welcome to state bank of india*****")
    print("1.create Account")
    print("2.Login")
    print("3.Exit")
    choice=input("Enter an option:")
    if choice=="1":
        bank.createaccount()
    elif choice=="2":
        account=bank.login()
        if account:
            while True:
                print("***welcome to state bank of india ATM ***")
                print("1.Deposit")
                print("2.withdraw")
                print("3.check balance")
                print("4.mini statement")
                print("5.Logout")
                sub_choice=input("Enter your choice:")
                if sub_choice=="1":
                    bank.deposit(account)
                elif sub_choice=="2":
                    bank.withdraw(account)
                elif sub_choice=="3":
                    bank.check_balance(account)
                elif sub_choice=="4":
                    bank.mini_statement(account)
                elif sub_choice=="5":
                    print("Log out successfully")
                    break
                else:
                    print("Invaliod user choice.try again")
    elif choice=="3":
        bank.exit()
    else:
        print("Invalid user choice ....Please try again")
                    
                    
        
    


            
            
        