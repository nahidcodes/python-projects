import random

def menu():
    print()
    print("0 - exit")
    print("1 - rock")
    print("2 - scissors ")
    print("3 - paper")
    print("4 - statistics")
    print()

def pause():
    input("Press Enter...")


def choose():
    ch=None
    
    while ch is None:
        try:
            ch=int(input("Enter the number from 0 to 4: "))

            if ch not in [0, 1, 2, 3, 4]:
                print("Incorrect number")
                continue

        except ValueError:
            print("NUMBER!")

        if ch==1:
            print()
            print("You choosed: rock")
            print()
        elif ch==2:
            print()
            print("You choosed: scissors")
            print()
        elif ch==3:
            print()
            print("You choosed: paper")
            print()

    return ch

def komp_choose():
    komp=random.randint(1, 3)
    return komp

def kompot(komp):
    if komp==1:
        print("Komputer choosed: rock")
        print()
    elif komp==2:
        print("Komputer choosed: scissors")
        print()
    else:
        print("Komputer choosed: paper")
        print()

games=0
wins=0
losses=0
draws=0
percentage=0


def win(wins):
    print("You won!")
    wins+=1
    print()
    pause()
    return wins

def lost(losses):
    print("You lost!")
    losses+=1
    print()
    pause()
    return losses

def draw(draws):
    print("Draw")
    draws+=1
    print()
    pause()
    return draws

def game(games, wins, losses, draws):
    games=wins+losses+draws
    return games

def wins_percentage(percentage, wins, games):
    try:
        percentage=wins/games*100
    except ZeroDivisionError:
        pass
    return percentage

def statistics(wins, losses, draws, games, percentage):
    games=game(games, wins, losses, draws)
    percentage=wins_percentage(percentage, wins, games)
    print()
    print(f"Games: {games}")
    print(f"Wins: {wins}")
    print(f"Losses: {losses}")
    print(f"Draws: {draws}")
    print(f"Wins percentage: {percentage:.1f}%")
    print()
    pause()


while True:
    menu()

    ch=choose()
    komp=komp_choose()


    if ch==0:
        print("Game ended")
        break

    elif ch==komp:
        kompot(komp)
        draws=draw(draws)

    elif ch==1 and komp==2 or ch==2 and komp==3 or ch==3 and komp==1:
        kompot(komp)
        wins=win(wins)
    elif ch==1 and komp==3 or ch==2 and komp==1 or ch==3 and komp==2:
        kompot(komp)
        losses=lost(losses)
    elif ch==4:
        statistics(wins, losses, draws, games, percentage)

    
        
        
    
