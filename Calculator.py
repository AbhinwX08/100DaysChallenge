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

def addition(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def Multiply(n1,n2):
    return n1*n2

def Divide (n1,n2):
    return n1/n2

dictionary= {}
calc_work= True

while calc_work:

    n1= float(input("Enter your first number: "))
    operation= int(input("Enter the number for the operation you wanted to do: \n1. Addition\n2. Substraction\n3. Multiply\n4. Divide\n"))
    n2= float(input("Enter your second number: "))
    
    if operation==1:
        dictionary['+']= addition(n1,n2)
        print(dictionary['+'])

    elif operation==2:
        dictionary['-']= substract(n1,n2)
        print(dictionary['-'])

    elif operation==3:
        dictionary['*']= Multiply(n1,n2)
        print(dictionary['*'])

    elif operation==4:
        dictionary['/']= Divide(n1,n2)
        print(dictionary['/'])

    else:
        print("Enter valid choice!!")

    choice= input("Enter 'y' for yes to continue or 'n' for no to discontinue the operations: ")
    if choice=="n":
        calc_work= False
        print("Operations over, Bye!!")

    elif choice=='y':
        pass

    else:
        print("Enter valid entry...")
    

print(dictionary)