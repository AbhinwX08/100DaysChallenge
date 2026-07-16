calculator= (r''' 
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

calc_work= True

while calc_work:

    n1= float(input("Enter your first number: "))
    print("1. Addition\n2. Substraction\n3. Multiply\n4. Divide\n")
    operation_choice= int(input("Enter the choice for the operation you wanted to do: "))
    n2= float(input("Enter your second number: "))
    
    if operation_choice in dictionary:
        calc_function= dictionary[operation_choice]
        answer= calc_function(n1,n2)

        print(f"The answer is= {answer}")
    else:
        print("Enter valid input")

    choice= input("Enter 'y' for yes to continue or 'n' for no to discontinue the operations: ")
    if choice=="n":
        calc_work= False
        print("Operations over, Bye!!")

    elif choice=='y':
        pass

    else:
        print("Enter valid entry...")
    

print(dictionary)