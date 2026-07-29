import random
import sys

class Random_word:
    def __init__(self, hp=5):
        self.word=random.choice(["python", "java", "fuck"])
        self.guessed_letters=[]
        self.hp=hp

    def show_lines(self):
        won=True
        not_guessed="_"
        print()
        for i in self.word:
            if i not in self.guessed_letters:
                won=False
            if i in self.guessed_letters:
                print(i, end=" ")
            else:
                print(not_guessed, end=" ")

        if won:
            print("\nYOU WON!")
            sys.exit()
        print()


    def guess_letter(self):
        qwer=False
        
        while not qwer:
            guess=input("\nEnter letter: ")

            if len(guess.strip())!=1:
                print("Incorrect enter")
            else:
                qwer=True
                break

        if guess in self.guessed_letters:
            print("You already entered this fucking letter")
            return


        if guess in self.word:
            print("\nYes")
            self.guessed_letters.append(guess)
            
            self.show_lines()

       
        else:
            print("\nNo")
            self.hp-=1
            print("HP:", self.hp)
            self.show_lines()

            if self.hp<=0:
                self.hp=0
                print("YOU LOSE")
                sys.exit()
        

asdf=Random_word()
asdf.show_lines()
while True:
    asdf.guess_letter()