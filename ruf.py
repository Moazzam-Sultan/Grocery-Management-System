import csv

# Sample data: List of products
   
products = [
    ["P001", "Apple", "Fruits", 3, 100],
    ["P002", "Banana", "Fruits", 1, 200],
    ["P003", "Carrot", "Vegetables", 2, 150],
    ["P004", "Broccoli", "Vegetables", 2.5, 80],
    ["P005", "Chicken Breast", "Meat", 5, 50],
    ["P006", "Ground Beef", "Meat", 6, 40],
    ["P007", "Milk", "Dairy", 2, 60],
    ["P008", "Cheese", "Dairy", 4, 30],
    ["P009", "Eggs", "Dairy", 3, 120],
    ["P010", "Bread", "Bakery", 2, 70],
    ["P011", "Butter", "Dairy", 3.5, 40],
    ["P012", "Rice", "Grains", 1.5, 150],
    ["P013", "Pasta", "Grains", 1.8, 100],
    ["P014", "Cereal", "Grains", 4, 50],
    ["P015", "Tomato", "Vegetables", 2.2, 90],
    ["P016", "Potato", "Vegetables", 1.5, 180],
    ["P017", "Onion", "Vegetables", 1.8, 140],
    ["P018", "Orange Juice", "Beverages", 3.5, 50],
    ["P019", "Coffee", "Beverages", 5, 40],
    ["P020", "Tea", "Beverages", 4, 60]
]
# Write the list to a CSV file
with open('products.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(products)



# Read the list from the CSV file
with open('products.csv', mode='r') as file:
    reader = csv.reader(file)
    read_products = list(reader)

# Display the read data
    
    
    customers = [
    ["C001", "Moazzam", 19, "mzzm@example.com", []],
    ["C002", "Mudassar", 20, "mudassar@example.com", []],
    ["C003", "noor", 17, "noor@example.com", []],
    ["C004", "Ans", 28, "ans@example.com", []],
    ["C005", "Uzair", 40, "uzir@example.com", []],
    ["C006", "Sultan", 22, "sultan@example.com", []],
    ["C007", "Aslam", 33, "aslam@example.com", []],
    ["C008", "Hannan", 27, "hannan@example.com", []],
    ["C009", "sam", 31, "sam@example.com", []],
    ["C010", "yusuf", 29, "yusuf@example.com", []]
]
    # Write the list to a CSV file
with open('customers.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(customers)



# Read the list from the CSV file
with open('customers.csv', mode='r') as file:
    reader = csv.reader(file)
    read_customers = list(reader)

# Display the read data
