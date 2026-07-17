calculator_art= (r''' 
_______________________
|  _________________  |
| | AU           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
             
''')

def Addition(n1,n2):
    return n1+n2                   

def Substract(n1,n2):
    return n1-n2

def Multiply(n1,n2):
    return n1*n2

def Divide (n1,n2):
    return n1/n2

dictionary= {
    1: Addition,
    2: Substract,
    3: Multiply, 
    4: Divide
}

def calculator():      
    calc_work= True
    num1= float(input("Enter your first number: "))

    while calc_work:

        print("1. Addition\n2. Substraction\n3. Multiply\n4. Divide\n")
        operation_choice= int(input("Pick an operation : "))
        num2= float(input("Enter your second number: "))
        
        if operation_choice in dictionary:
            calc_function= dictionary[operation_choice]
            answer= calc_function(num1,num2)
            print(f"The answer is= {answer}")

        else:
            print("Enter valid input")
            continue

        choice= input(f"Enter 'y' for yes to continue with exisitng result {answer} or 'n' for no to start for the new calculation ").lower()
        
        if choice=='y':
            num1==answer
        elif choice=='n':
            calc_function=False
            print("\n"*20)
            calculator()
        else:
            print("Enter valid input!!")
            continue

calculator()