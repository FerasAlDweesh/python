from datetime import datetime

def check_birthdate(year, month, day):
	todays_date = datetime.now()
	birthdate = datetime(birth_year, birth_month, birth_day)
	if birthdate > todays_date:
		return False
	else:
		return True

def calculate_age(year, month, day):
	todays_date = datetime.now()
	birthdate = datetime(birth_year, birth_month, birth_day)
	age = todays_date - birthdate
	print("you are %d years old" % (age.days / 365))

birth_year = int(input("Enter the year you were born:  "))
birth_month = int(input("Enter the month you were born:  "))
birth_day = int(input("Enter the day you were born:  "))

if check_birthdate(birth_year, birth_month, birth_day):
	calculate_age(birth_year, birth_month, birth_day)
else:
	print("Invalid date")
