import sys

name = input("Enter the item's name, enter done when finished: ")
price = input("Enter the item's price: ")
quantity = input("Enter the item's quantity: ")

while name != "done":
	name = input("Enter another item, enter done when finished: ")
	if name == "done":
		sys.exit("Thank you for shopping with us!")
	price = input("Enter the item's price: ")
	quantity = input("Enter the item's quantity: ")

shopping_list = []
item = {"name" : name, "price" : price, "quantity" : quantity}

item["name"] = name
item["price"] = price
item["quantity"] = quantity

for receipt in shopping_list:
	print("receipt")
	print(quantity, name, price)
	print("Total Price: ", sum(price))