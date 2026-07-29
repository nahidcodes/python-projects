import random
import time

class Casino:
    def __init__(self, balance=0):
        self.balance=balance

    def show_balance(self):
        print()
        print("Balance:", str(self.balance)+"$")
        print()

    def pause(self):
        input("Press Enter...")

    def slots(self):
        bet=self.get_bet()

        symbols=["A", "B", "C", "7"]
        

        a=random.choice(symbols)
        b=random.choice(symbols)
        c=random.choice(symbols)

       

        print()
        print(a, b, c)
        print()


        if a==b==c:
            print("-----!!!JACKPOT!!!-----")
            print(f"-----YOU WON {bet*10}$-----")
            self.balance+=bet*10
            self.show_balance()
            self.save_balance()

        elif a==b or b==c or a==c:
            print("-----Nice!-----")
            print(f"--You won {bet*2}$--")
            self.balance+=bet*2
            self.show_balance()
            self.save_balance()


        else:
            print(f"Ti proyebal {bet}$")
            self.show_balance()
            self.save_balance()


        self.pause()
            
       
    
    def roulette(self):
        bet=self.get_bet()

        print()
        print("Choose:")
        print("1 - Red")
        print("2 - Black")
        print()

        choice=random.randint(1, 2)

        br=None
        
        while br!=1 and br!=2:
            try:

                br=int(input("Enter the number: "))
                print()

                if br not in [1, 2]:
                    print("Incorrect number")
                    print()

            except ValueError:
                print("NUMBER!")

        print("Rolling...")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print()

       

        if choice==1:
            print("Roulette: Red")
            print()
        else:
            print("Roulette: Black")
            print() 
        

        if choice==br:
            print(f"You won {bet*2}$!") 
            print()
            self.balance+=bet*2
            self.show_balance()
            self.save_balance()


        else:
            print(f"Ti proyebal {bet}$")
            self.show_balance()
            self.save_balance()


        self.pause()
    
    def get_bet(self):
         self.show_balance()

         bet=999999999999999

         while bet>self.balance or bet<=0:
            try:
                bet=int(input("Enter your bet: "))

                if bet>self.balance:
                    print("Not enough money!")

                if bet<=0:
                    print("Bet must be greater than 0!")
                    continue

            except ValueError:
                print("NUMBER!")

            
         self.balance-=bet
         return bet
    
    def load_balance(self):
        try:
            with open("balance.txt", "r") as file:
                money=int(file.read())
                self.balance=money
        except FileNotFoundError:
            print("File not found. Starting with 100$")

    def save_balance(self):
        with open("balance.txt", "w") as file:
            file.write(str(self.balance))
                        


kazik=Casino(100)
kazik.load_balance()



def menu():
    print()
    print("0 - Exit")
    print("1 - Slots")
    print("2 - Roulette")
    print("3 - Balance")
    print()



while True:
    menu()

    a=input("Enter the number from 0 to 3: ")
    print()

    if a=="0":
        print("Bye!")
        break

    elif a=="1":
        kazik.slots()

    elif a=="2":
        kazik.roulette()

    elif a=="3":
        kazik.show_balance()

    else:
        print("Unknown command")

    

