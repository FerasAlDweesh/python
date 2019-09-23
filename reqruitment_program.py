skills = ["writing",
          "reading",
          "speaking",
          "programming",
          "bilingual"
          ]

print(skills)

cv = {}
name = input("Please enter your name:  ")
age = input("Please enter your age:  ")
experience = input("How many years of experience do you have?  ")
cv["name"] = name
cv["age"] = age
cv["experience"] = experience

print("Choose any of the skills below: ")
for skill in skills:
	x = skills.index(skill) + 1 
	print(x, skill)

first_skill = input("Choose a skill from the list:  ")
second_skill = input("Choose another skill from the list: ")

cv["first skill"] = first_skill
cv["second skill"] = second_skill

print("This is what your applications looks like:", cv)


if age >= "21":
	print("You are old enough to apply!")
elif age < "21":
	print("You are not old enough to apply!")

if experience >= "3":
	print("You have enough experience for the job.")
elif experience < "3":
	print("You don't have enough experience for this job!")

if "writing" and " programming" in cv.items():
	print("Congratulations, you have been accepted!")