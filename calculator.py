first_number = input("Enter a first number:  ")
second_number = input("Enter a second number:  ")
operation = input("Enter a math operation (+, -, *, /):  ")
if first_number.isdigit() and second_number.isdigit() == False:
	print("The numbers are invalid!")
elif operation == "+":
	print(int(first_number) + int(second_number))
elif operation == "-":
	print(int(first_number) - int(second_number))
elif operation == "*":
	print(int(first_number) * int(second_number))
elif operation == "/":
	print(int(first_number) / int(second_number))
else:
	print("The operation is not valid")