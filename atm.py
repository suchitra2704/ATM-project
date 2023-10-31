import sys
class Atm():
    def __init__(self):
        self.pin=1234
        self.balance=20000
        self.Menu()

    def Menu(self):
        print('''which oeration you want to do
                            
                            1.balance enquiry
                            2.withdraw
                            3.deposit
                            4 quit
                        ''')
        option=int(input("enter your option"))
        if option==1:
            self.Check_balance()
        elif option==2:
            self.Withdraw()
        elif option==3:
            self.Deposit()
        elif option==4:
            sys.exit()
        else:
            print("input right option")
    def Check_balance(self):
        your_pin = int(input("enter your pin"))
        if your_pin == self.pin:
            print(f"your balance is{self.balance}")
            print("*"*50)
        else:
            print("enter valid pin")
        self.Menu()
    def Withdraw(self):
        your_pin = int(input("enter your pin"))
        if your_pin == self.pin:
            withdraw_money=int(input("how much money you want to withdraw?"))
            if withdraw_money <= self.balance:
                your_money = self.balance - withdraw_money
                print("money is your's", your_money, "/n current balance is", self.balance)

            else:
                print("insufficient balance")
        self.Menu()

    def Deposit(self):
        your_pin = int(input("enter your pin"))
        if your_pin == self.pin:
            deposit=int(input("how much you want to deposite"))
            card_no=int(input("enter your  16 digit card no"))
            if card_no==1234567890123456:
                print("you deposte",deposit)
                print("now your balance is" , deposit+self.balance)
            else:
                print("please enter valid card no")
        else:
            print("enter valid pin no")
        self.Menu()




obj=Atm()


