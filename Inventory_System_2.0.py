import json

def menu():
    print("\n1 - Show inventory")
    print("2 - Add item")
    print("3 - Remove item")
    print("4 - Add gold")
    print("5 - Show gold")
    print("0 - Exit")
    

try:
    with open("inventory.json", "r") as file:
       data=json.load(file)
       gold=data["gold"]
       inventory=data["inventory"]
except FileNotFoundError:
    inventory={}
    gold=0


while True:
    menu()
    ch=input("\nChoice: ")

    if ch=="0":
        data={
            "gold": gold,
            "inventory": inventory
        }

        with open("inventory.json", "w") as file:
            json.dump(data, file, indent=4)

        print("\nGoodbye!")
        break

    elif ch=="1":
        if not inventory:
            print("\nInventory is empty!")
        else:
            print()
            for key, value in inventory.items():
                print(key, "-", value)
        
    elif ch=="2":
        item=input("Item: ")

        if item in inventory:
            inventory[item]+=1
        else:
            inventory[item]=1

    elif ch=="3":
        item=input("Item: ")

        if item in inventory:
            inventory[item]-=1

            if inventory[item]>0:
                print("\n"+item, "-", inventory[item])

            else: 
                print("\n"+item, "removed from inventory")
                del inventory[item]

        else:
            print("\nItem not found")

    elif ch=="4":
        add_gold=None

        while add_gold is None:
            try:
                add_gold=int(input("\nHow many gold?: "))
            except ValueError:
                print("Enter number!")

        gold+=add_gold

    elif ch=="5":
        print("\nGold:", gold)

        
