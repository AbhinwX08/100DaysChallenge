print("Tip calculator")
bill= int(input("Enter the total bill of the dinner (in $): \n"))
tip= int(input("What percentage of tip would you like to give? (e.g: 10, 12, 15): \n"))
persons= int(input("Number of persons had dinner: \n"))

calc= (bill*tip/100)+bill
final_bill= round(calc/persons,2)

print(f"Each person have to pay: ${final_bill}")