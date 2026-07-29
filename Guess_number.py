import random
import sys

class Guess_number:
    def __init__ (self, x=random.randint(1, 10), attempts=1, guess=999999999999):
        self.x=x
        self.attempts=attempts
        self.guess=guess


    def game(self):

        while self.attempts<4:
            try:
                self.guess=int(input("\nEnter the number from 1 to 10: "))

                if self.guess==self.x:
                    print("YOU WON!")
                    print(f"Guessed for {self.attempts} attempts")
                    break

                elif self.guess>self.x:
                    print("Smaller!")
                    self.attempts+=1
                else:
                    print("Bigger!")
                    self.attempts+=1
            except ValueError:
                print("NUMBER!")



        else:
            print("YOU LOSE NAXUY!")


    def again(self):
        self.attempts=1
        self.x=random.randint(1, 10)
        print()
        print("Play again?")
        print("1 - yes")
        print("2 - no")
        print()

        self.play=0

        while self.play not in [1, 2]:
            try:
                self.play=int(input("Enter 1 or 2: "))

                if self.play not in [1, 2]:
                    print("Incorrect number")
                    continue

            except ValueError:
                print("NUMBER!")
                continue

            if self.play==1:
               self.game()
            else:
                print("Bye!")
                sys.exit()



game=Guess_number()
game.game()
while True:
    game.again()

