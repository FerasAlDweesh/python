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

# skill_set = []
cv["skill_set"] = []

print("Choose any of the skills below: ")
for skill in skills:
	x = skills.index(skill) + 1 
	print(x, skill)


first_skill = input("Choose a skill from the list:  ")
second_skill = input("Choose another skill from the list: ")


cv["skill_set"].append(skills[int(first_skill) - 1]) 
cv["skill_set"].append(skills[int(second_skill) - 1])



print("This is what your applications looks like:", cv)



if cv["age"] >= "21":
	print("You are old enough to apply!")
elif cv["age"] < "21":
	print("You are not old enough to apply!")

if cv["experience"] >= "3":
	print("You have enough experience for the job.")
elif cv["experience"] < "3":
	print("You don't have enough experience for this job!")


if "writing" in cv["skill_set"] and "programming" in cv["skill_set"]:
	print("Congratulations, you have been accepted!")
else:
	print("Sorry, you do not have the skills required for the job!")




# if michael's age > 5 and steven's age > 5: