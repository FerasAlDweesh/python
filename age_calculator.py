from datetime import date
todays_date = date.today()
print("Today's date is", todays_date)

birth_year = int(input("Enter the year you were born:  "))
birth_month = int(input("Enter the month you were born:  "))
birth_day = int(input("Enter the day you were born:  "))


def check_birthdate(year, month, day):
	if birth_year > todays_date:
		return False

def calculate_age(year, month, day):
	age = date.year() - birth_year


print("you are", calculate_age(birth_year, birth_month, birth_day), "years old")
