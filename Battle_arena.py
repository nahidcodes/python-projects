import time
import random


class Character:
    def __init__(self, name="Unknown", hp=0, damage=0, potions=3):
        self.name=name
        self.hp=hp
        self.damage=damage
        self.potions=potions

    def show(self):
        print("Name:", self.name)
        print("HP:", self.hp)
        print("Damage:", self.damage)
        print("Potions:", self.potions)

    def attack(self, enemy):
        real_damage=random.randint(self.damage-5, self.damage+5)

        print(self.name, "attacks", enemy.name+"!")
        print("Damage:", real_damage)

        enemy.take_damage(real_damage)
        print()

    def take_damage(self, damage):
        self.hp-=damage

        if self.hp<=0:
            self.hp=0
            print(self.name, "lost!")
        else:
            print(self.name, "HP:", self.hp)
        print()

    def heal(self):
        if self.potions>0:
            self.potions-=1
            self.hp+=20

            if self.hp>100:
                self.hp=100

            print(self.name, "healed!")
            print("HP:", self.hp)
            print("Potions:", self.potions)
            print()

        else:
            print("No potions!")
            print()

    def special(self, enemy):
        pass


class Warrior(Character):
    def __init__(self, name, hp, damage, potions, armor):
        super().__init__(name, hp, damage, potions)
        self.armor=armor

    def show(self):
        super().show()
        print("Armor:", self.armor)
        print()

    def take_damage(self, damage):
        if self.armor>=damage:
            print(self.name, "blocked the damage!")
            self.armor-=damage
            print("Armor:", self.armor)
        else:
            taken_damage=damage-self.armor
            self.armor=0
            self.hp-=taken_damage

            if self.hp<=0:
                self.hp=0
                print(self.name, "lost!")
            else:
                print(self.name, "HP:", self.hp)

    def restore_armor(self):
        self.armor+=20

        if self.armor>40:
            self.armor=40

        print(self.name, "restored armor!")
        print("Armor:", self.armor)
        print()

    def special(self, enemy):
        self.restore_armor()


class Mage(Character):
    def __init__(self, name, hp, damage, potions, mana):
        super().__init__(name, hp, damage, potions)
        self.mana=mana

    def show(self):
        super().show()
        print("Mana:", self.mana)
        print()

    def fireball(self,enemy):
        if self.mana>=20:
            self.mana-=20
            print(self.name, "casts fireball on", enemy.name+"!")
            enemy.take_damage(self.damage*2)
            print()

        else:
            print("Not enough mana!")
            print()

    def special(self, enemy):
        self.fireball(enemy)


class Archer(Character):
     def __init__(self, name, hp, damage, potions, arrows):
        super().__init__(name, hp, damage, potions)
        self.arrows=arrows

     def show(self):
         super().show()
         print("Arrows:", self.arrows)
         print()

     def shoot(self, enemy):
         real_damage=random.randint(self.damage-5, self.damage+5)

         if self.arrows>0:
             self.arrows-=1

             print(self.name, "shoots", enemy.name+"!")
             print("Damage:", real_damage)
             print()

             enemy.take_damage(real_damage)

         else:
             print("No arrows!")
             print()

     def special(self, enemy):
         self.shoot(enemy)



             
warrior=Warrior("BIG", 100, 30, 3, 40)
mage=Mage("MAQA", 100, 35, 3, 40)
archer=Archer("ARCHA", 100, 25, 3, 12)



def enemy_turn(enemy, player):
    x=random.randint(1, 3)

    if x==1:
       enemy.attack(player)
    elif x==2:
        enemy.heal()
    else:
        enemy.special(player)


warrior.show()
mage.show()
archer.show()
       

print("Choose your hero:")
print()
print("1 - Warrior")
print("2 - Mage")
print("3 - Archer")
print()

hero=0

while hero==0:
    try:
        hero=int(input("Enter the number from 1 to 3: "))

        if hero==1:
            player=warrior
        elif hero==2:
            player=mage
        elif hero==3:
            player=archer
        else:
            print("Unknown hero!")
            hero=0
            

    except ValueError:
        print("NUMBER!")

print()
print("Your hero is:", player.name)
print()


print("Choose enemy:")
print()
print("1 - Warrior")
print("2 - Mage")
print("3 - Archer")
print()

en=0

while en==0:
    try:
        en=int(input("Enter the number from 1 to 3: "))

        if en==1:
            enemy=warrior
        elif en==2:
            enemy=mage
        elif en==3:
            enemy=archer
        else:
            print("Unknown enemy!")
            en=0
            continue

        if en==hero:
            print("You can`t fight yourself!")
            en=0
            continue
    
            
    except ValueError:
        print("NUMBER!")

print()
print("Your enemy is:", enemy.name)
print()
time.sleep(0.5)

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

print()
print()
print("-----GAME STARTED NAXUY-----")
print()



while player.hp>0 and enemy.hp>0:

    print("1 - Attack")
    print("2 - Special")
    print("3 - Heal")
    print("4 - Stats")
    print()

    action=input("Enter the number from 1 to 4: ")
    print()

    if action=="1":
        player.attack(enemy)
        time.sleep(1)
        if enemy.hp>0:
            enemy_turn(enemy, player)
           
    elif action=="2":
        player.special(enemy)
        
        if enemy.hp>0:
            enemy_turn(enemy, player)

                
    elif action=="3":
        if player.potions>0:
            player.heal()
            time.sleep(1)
            enemy_turn(enemy, player)
            time.sleep(1)
        else:
            print("No potions!")

    elif action=="4":
        player.show()
        enemy.show()

    else:
        print("Unknown command")

        
    
if player.hp>0:
    print("YOU WIN!")
else:
    print("YOU LOSE NAXUY!")
   
   

            

            
