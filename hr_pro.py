from datetime import datetime
import sys


today = datetime.today()

class Employee:
	def __init__(self, name, age, salary, employement_date):
		self.name = name
		self.age = age
		self.salary = salary
		self.employement_date = employement_date

	def get_working_years(self):
		experience = today.year - int(self.employement_date)
		return experience

	def __str__(self):
		return ("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s") % ("Name: ", self.name, "Age: ", self.age, "Salary: ", self.salary, "Employeed since: ", self.employement_date, "Years of experience: ", self.get_working_years())

class Manager(Employee):
	def __init__(self, name, age, salary, employement_date, bonus_percentage):
		Employee.__init__(self, name, age, salary, employement_date)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		bonus = int(self.salary) * (int(self.bonus_percentage) / 100)
		return bonus

	def __str__(self):
		return ("%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s") % ("Name: ", self.name, "Age: ", self.age, "Salary: ", self.salary, "Employeed since: ", self.employement_date, "Years of experience: ", self.get_working_years(), "Bonus: ", self.get_bonus())


print("Welcome to HR Pro 2019, choose an option:")
options = ["Show Employees", "Show Managers", "Add an Employee", "Add a manager", "Exit"]
for option in options:
	x = options.index(option) + 1 
	print(x, option)

# Had to define choice before entering it into a loop as an input sp used empty string

choice = print("")

employees_list = []
managers_list = []

while choice != "5":
	choice = input("Choose a number from the list above: ")

	if choice == "1":
		for e in employees_list:
			print(e)

	if choice == "2":
		for m in managers_list:
			print(m)
		
	if choice == "3":
		user_name = input("Enter name: ")
		user_age = input("Enter age: ")
		user_salary = input("Enter salary: ")
		user_date = input("Enter year: ")

		person1 = Employee(user_name, user_age, user_salary, user_date) 
		employees_list.append(person1)

	if choice == "4":
		user_name = input("Enter name: ")
		user_age = input("Enter age: ")
		user_salary = input("Enter salary: ")
		user_date = input("Enter year: ")
		bonus_percentage = input("Enter bonus: ")
		print("Manager added succesfully!")

		person2 = Manager(user_name, user_age, user_salary, user_date, bonus_percentage)
		managers_list.append(person2)

	if choice == "5":
		sys.exit()
