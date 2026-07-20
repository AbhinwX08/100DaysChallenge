import Coffee_data

print(Coffee_data.logo)
print("\nWelcome to the world of making coffee!!")

Machine_report= input("Before making coffee do you want to see the available ingredients present in the machine?\nEnter 'y' for yes and 'n' for no: ").lower()
if Machine_report=='y':
    print (f"Milk (in ml): {Coffee_data.Machine['Milk']},Cofee (in gm): {Coffee_data.Machine['Coffee']} and Water (in ml): {Coffee_data.Machine['Water']}")
elif Machine_report=='n':
    print("Continue making your coffee!!")
else:
    print("Enter valid input!!")

print("We have all these types of coffee with their prices, Please select anyone type from the list given below :)")

for key in Coffee_data.Types:
    print(f"Coffee type: {key} and its Price (in ₹): {Coffee_data.Types[key]}")
