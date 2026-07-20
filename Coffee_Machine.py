import Coffee_data

print(Coffee_data.logo)
print("\nWelcome to the world of making coffee!!")

Coffee_continue=True
while Coffee_continue:

    Machine_report= input("Before making coffee do you want to see the available ingredients present in the machine?\nEnter 'y' for yes and 'n' for no: ").lower()
    if Machine_report=='y':
        print (f"Milk (in ml): {Coffee_data.Machine['Milk']}, Coffee (in gm): {Coffee_data.Machine['Coffee']} and Water (in ml): {Coffee_data.Machine['Water']}\n")

    elif Machine_report=='n':
        print("Continue making your coffee!!\n")

    else:
        print("Enter valid input!!")

    print("---------------------------COFFEE LIST---------------------------\n")

    for key in Coffee_data.Types:
        print(f"Coffee type: {key} and its Price (in ₹): {Coffee_data.Types[key]}\n")

    choice= int(input("Your coffee number (in 1/2/3 number): "))
    print("Use only coins to get your coffee!!")
        
    coins_10= int(input("₹10 coin: "))
    coins_20= int(input("₹20 coin: "))
    coins_50= int(input("₹50 coin: "))
    price_of_coffee= coins_10*10 + coins_20*20 + coins_50*50

    if choice==1:
        condition= Coffee_data.Machine['Milk']>=Coffee_data.Coffee_ingredients[0]['Milk'] and Coffee_data.Machine['Coffee']>=Coffee_data.Coffee_ingredients[0]['Coffee'] and Coffee_data.Machine['Water']>=Coffee_data.Coffee_ingredients[0]['Water']
        if condition:
            print(f"Your choosen coffee is: Espresso\nPay (₹):{Coffee_data.Types['Espresso']}")
            if price_of_coffee>=Coffee_data.Types['Espresso']:
                print("Enjoy the sip of your coffee!!")
                Coffee_data.Machine['Milk']-=0
                Coffee_data.Machine['Water']-=60
                Coffee_data.Machine['Coffee']-=18
            else:
                print("Not enough money, Refund initiated..\nPlease give sufficicient money to intiate the process of making coffee!!")
        else:
            print("There is shortage of ingredients in the machine so cant make coffee right now!!\nSorry for the inconvenience")

    elif choice==2:
        condition= Coffee_data.Machine['Milk']>=Coffee_data.Coffee_ingredients[1]['Milk'] and Coffee_data.Machine['Coffee']>=Coffee_data.Coffee_ingredients[1]['Coffee'] and Coffee_data.Machine['Water']>=Coffee_data.Coffee_ingredients[1]['Water']
        if condition:
            print(f"Your choosen coffee is: Latte\nPay (₹):{Coffee_data.Types['Latte']}")
            if price_of_coffee>=Coffee_data.Types['Latte']:
                print("Enjoy the sip of your coffee!!")
                Coffee_data.Machine['Milk']-=240
                Coffee_data.Machine['Water']-=60
                Coffee_data.Machine['Coffee']-=18
            else:
                print("Not enough money, Refund initiated..\nPlease give sufficicient money to intiate the process of making coffee!!")
        else:
            print("There is shortage of ingredients in the machine so cant make coffee right now!!\nSorry for the inconvenience")
    
    elif choice==3:
        condition= Coffee_data.Machine['Milk']>=Coffee_data.Coffee_ingredients[2]['Milk'] and Coffee_data.Machine['Coffee']>=Coffee_data.Coffee_ingredients[2]['Coffee'] and Coffee_data.Machine['Water']>=Coffee_data.Coffee_ingredients[2]['Water']
        if condition:
            print(f"Your choosen coffee is: Cappuccino\nPay (₹):{Coffee_data.Types['Cappuccino']}")
            if price_of_coffee>=Coffee_data.Types['Cappuccino']:
                print("Enjoy the sip of your coffee!!")
                Coffee_data.Machine['Milk']-=120
                Coffee_data.Machine['Water']-=60
                Coffee_data.Machine['Coffee']-=18
            else:
                print("Not enough money, Refund initiated..\nPlease give sufficicient money to intiate the process of making coffee!!")
        
        else:
            print("There is shortage of ingredients in the machine so cant make coffee right now!!\nSorry for the inconvenience")

    else:
        print("Enter valid choice!!")

    Coffee_making= input("Do you want to make coffee again?\nEnter 'y' for yes and 'n' for no : ")
    if Coffee_making=='n':
        print("Thank You\nHave a nice day!!")
        Coffee_continue= False
    elif Coffee_making=='y':
        Coffee_continue= True

    else:
        print("Enter valid input")
        Coffee_continue=False