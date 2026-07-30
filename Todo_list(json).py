import json

def menu():
    print("""
1 - Show tasks
2 - Add task
3 - Remove task
4 - Complete task
0 - Exit""")

try:
    with open("TODO_list.json", "r") as file:
        tasks=json.load(file)
except FileNotFoundError:
    tasks=[]

while True:
    menu()
    ch=input("\nChoose: ")

    if ch=="0":
        with open("TODO_list.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("\nGoodbye!")
        break

    elif ch=="1":
        if not tasks:
            print("\nNo tasks!")
        else:
            print()
            for n, i in enumerate(tasks, start=1):
                if i["done"]:
                    print(f"{n}) ✔ {i['task']}")
                else:
                     print(f"{n}) ❌ {i['task']}")
                    
    elif ch=="2":
        add_task=input("\nTask: ")
        task_done={"task": add_task,
                   "done": False
                   }
        tasks.append(task_done)

    elif ch=="3":
        remove_task=None
        while remove_task is None:
            try:
                remove_task=int(input("\nTask: "))
                removed=tasks.pop(remove_task-1)
                print("\nRemoved:", removed["task"])
            except ValueError:
                print("Enter number!")
            except IndexError:
                print("Incorrect number!")
                remove_task=None

    elif ch=="4":
        complete_task=None
        while complete_task is None:
            try:
                complete_task=int(input("\nTask: "))
                if tasks[complete_task-1]["done"]:
                    print("\nTask already completed!")
                else:
                    tasks[complete_task-1]["done"]=True
                    print("\nCompleted:", tasks[complete_task-1]["task"])
            except ValueError:
                print("Enter number!")
            except IndexError:
                print("Incorrect number")
                complete_task=None

    else:
        print("\nUnknown command")
               

            