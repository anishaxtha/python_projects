# shopping cart using python 

items = input("What items would you like to buy: ")
price = float(input("What is the price of the items: "))
quantity = int(input("How many would you like: "))

total = price *quantity
print(f"You have brought {quantity} X {items}/s")
print(f"Your total is ${round(total,2)}")
