# Write a Python program to create a dictionary containing three products and their prices and perform the following operations:
# i. Display the dictionary. 
# ii. Display all product names. 
# iii. Display all product prices. 
# iv. Add a new product and its price. 
# v. Find the total price of all products.

products = {
    "Notebook": 50,
    "Pen": 10,
    "Bag": 800
}

print("Product dictionary:", products)
print("Product names:", list(products.keys()))
print("Product prices:", list(products.values()))

products["Pencil"] = 5
print("After adding Pencil:", products)

total_price = sum(products.values())
print("Total price of all products:", total_price)