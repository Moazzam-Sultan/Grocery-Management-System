
MAX_PRODUCTS = 20
MAX_CUSTOMERS = 10
MAX_ITEMS_PER_TRANSACTION = 5
LOW_STOCK_THRESHOLD = 5

with open ('product.csv',"r") as file :
  products = file.read()
 
with open ('customers.csv',"r") as file:
    customers = file.read()

while True:
    print("\nMain Menu")
    print("1. Display Products")
    print("2. Display Customers")
    print("3. Sell Products")
    print("4. Restock Products")
    print("5. Search Products")
    print("6. Search Customers")
    print("7. Generate Reports")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Products:")
        print(products)
    elif choice == "2":
        print("\nAvailable Customers:")
        print(customers)
        
    elif choice == "3":
        product_id = input("Enter the product ID: ")
        for product in products.splitlines():
            if product_id in product:
                quantity = int(input("Enter the quantity: "))
                if quantity <= int(product.split(",")[3]):
                    products = products.replace(product, product + ", Sold: " + str(quantity) + "\n")
                    print("Product sold successfully!")