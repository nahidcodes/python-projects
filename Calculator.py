import sys

def calc():
    a=None
    b=None
    op=None
    
    while a is None:
        try:
            a=float(input("First number: "))
            print()
            if a==0:
                print("Bye!")
                sys.exit()
        except ValueError:
            print("NUMBER!")
        
    while op not in ["+", "-", "*", "/"]:
        op=input("Operation (+ - * /): ")

        if op in ["+", "-", "*", "/"]:
            print()
        else:
            print("Unknown operation")

    while b is None:
        try:
            b=float(input("Second number: "))
        except ValueError:
            print("NUMBER!")

    
 

    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op=="/":
        if b==0:
            while b==0:
                print("Cannot divide by zero!")
                try:
                    b=float(input("Second number: "))
                except ValueError:
                    print("NUMBER!")
                
            return a/b

            
while True:
    print("\n---Calculator---")
    print("Enter 0 to exit")
    print()

    print("Result:", calc())   


