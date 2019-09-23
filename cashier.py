import math

name = input("Enter the item's name, enter done when finished: ")
# price = input("Enter the item's price: ")
# quantity = input("Enter the item's quantity: ")

shopping_list = []

while name != "done":
	# name = input("Enter another item, enter done when finished: ")
	# if name == "done":
	# 	break
	price = input("Enter the item's price: ")
	quantity = input("Enter the item's quantity: ")	
	item = {"name" : name, "price" : price, "quantity" : quantity}
	# item["name"] = name
	# item["price"] = price
	# item["quantity"] = quantity
	shopping_list.append(item)
	name = input("Enter another item, enter done when finished: ")

total = 0

print("RECEIPT")

for receipt in shopping_list:
	total += int(receipt["price"])
	print(receipt)

print("Total Price: ", total) #sum all prices