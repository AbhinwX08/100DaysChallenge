import Coffee_data

print(Coffee_data.logo)
print("\nWelcome to the world of making coffee!!")

Machine_report= input("Before making coffee do you want to see the available ingredients present in the machine?\nEnter 'y' for yes and 'n' for no: ").lower()
if Machine_report=='y':
    print(Coffee_data.Machine)
elif Machine_report=='n':
    print("Continue making your coffee!!")
else:
    print("Enter valid input!!")


print(f"We have all these types of coffee please select anyone type from the list given below :)\n{Coffee_data.Types}")
