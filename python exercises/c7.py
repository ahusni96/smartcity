selection = -1

while selection != 0:

	print()
	print("1. Celcius to Fahrenheit")
	print("2. Fahrenheit to Celcius")
	print("Select '0' to exit")

	selection = int(input("Pick a conversion: "))

	if selection == 1:
		C = int(input("Enter a value: "))

		F = (C * 9 / 5) + 32
		print("The converted value : {}".format(F))
	
	elif selection == 2:
		F = int(input("Enter a value: "))

		C = (F - 32) * ( 5 / 9)
		print("The converted value : {}".format(C))

	elif selection == 0:
		break

	else:
		print("Invalid selection!")