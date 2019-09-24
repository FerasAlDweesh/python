import math

name = input("Enter the item's name, enter done when finished: ")


shopping_list = []

while name != "done":

	price = int(input("Enter the item's price: "))
	quantity = int(input("Enter the item's quantity: "))
	item = {"name" : name, "price" : price, "quantity" : quantity}
	
	shopping_list.append(item)
	name = input("Enter another item, enter done when finished: ")

total = 0

print("RECEIPT")

for receipt in shopping_list:
	total += (receipt["price"] * receipt["quantity"])
	print(receipt["quantity"], receipt["name"],"=", (receipt["price"] * receipt["quantity"]), "KD")
	
	

print("Total Price: ", total, "KD")