print("Welcome to the tip calculator!")

first_input=True

while first_input:
	try:
		total_bill = round(float(input("What was the total bill?")),2)
		first_input=False
	except:
		print("Try again, you must only enter a numerical value representing the monetary amount.")

second_input=True

while second_input:
	try:
		percentage_tip=int(input("How much of a tip in terms of % of the total bill would you like to give? 10%, 12% or 15%?"))
		if percentage_tip in (10,12,15):
			second_input=False
		else:
			print("Please specify only 10 or 12 or 15.")
	except:
		print("Please input an integer of value  10 or 12 or 15")

third_input=True

while third_input:
	try:
		num_splitting_bill=int(input("How many people to split the bill?"))
		third_input=False
	except:
		print("Please enter an integer value.")

bill = round(total_bill*(1+(percentage_tip/100))/num_splitting_bill,2)

print(f"Each person should pay: ${bill}")
