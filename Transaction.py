transactions = [
    ("2026-09-01", "A101", "Laptop", 2, 75000),
    ("2026-09-02", "A102", "Mouse", 10, 1200),
    ("2026-09-03", "A101", "Laptop", 1, 75000),
    ("2026-09-04", "A103", "Keyboard", 5, 2500),
    ("2026-09-05", "A102", "Mouse", 8, 1200),
]


def Product_Sales_Analysis(transactions):
    Product_sales={}
    for transaction in transactions:
        date, Customer_id, Product_name, Quantity, Product_Price = transaction;
        if Product_name not in Product_sales:
            Product_sales[Product_name]={
                "Total_Quantity": 0,
                "Total_Revenue": 0
            }
        Product_sales[Product_name]["Total_Quantity"] += Quantity
        Product_sales[Product_name]["Total_Revenue"] += Quantity * Product_Price

    print("========== PRODUCT SALES REPORT ==========")
    print(f"{"Product":<15}{"Quantity":<15}{"Revenue":<15}")
    print("-"*38)
    for product,details in Product_sales.items():
        print(f"{product:<15}{details["Total_Quantity"]:<15}{details["Total_Revenue"]:<15}")
    return Product_sales



def Product_Ranking(Product_sales):
    items=list(Product_sales.items())
    for i in range(len(items)):
        for j in range(len(items)-i-1):
            if items[j][1]['Total_Revenue']<items[j+1][1]['Total_Revenue']:
                items[j],items[j+1]=items[j+1],items[j]
            elif items[j][1]['Total_Revenue']==items[j+1][1]['Total_Revenue']:
                if items[j][1]['Total_Quantity']<items[j+1][1]['Total_Quantity']:
                    items[j],items[j+1]=items[j+1],items[j]
                elif items[j][1]["Total_Quantity"] == items[j + 1][1]["Total_Quantity"]:
                    if items[j][0]>items[j+1][0]:
                        items[j],items[j+1]=items[j+1],items[j]
    return items


def Top_Selling_Product(Transactions):
    max_selling=0
    for i in Transactions.keys():
        if Transactions[i]["Total_Quantity"]>max_selling:
            max_selling=Transactions[i]["Total_Quantity"]
            Product=i
    print("========== TOP-SELLING PRODUCT ==========")
    print()
    print("Product Name: ",Product)
    print("Total Quantity Sold: ",max_selling)


def Highest_Revenue_Product(Transactions):
    max_Revenue=0
    for i in Transactions.keys():
            if Transactions[i]["Total_Revenue"]>max_Revenue:
                max_Revenue=Transactions[i]["Total_Revenue"]
                Product=i
    print("========== HIGHEST-REVENUE PRODUCT ==========")
    print()
    print("Product :",Product)
    print("Revenue :",max_Revenue)


def Customer_Sales_Analysis(transactions):
    Customers={}
    for transaction in transactions:
        date, Customer_id, Product_name, Quantity, Product_Price = transaction;
        if Customer_id not in Customers:
            Customers[Customer_id]={
                "Total_Revenue":0
            }
        Customers[Customer_id]["Total_Revenue"]+= Quantity*Product_Price
    print("========== TOP 3 CUSTOMERS ==========")
    print()
    print(f"{"Rank":<15}{"Customer Id":<15}{"Purchase Value":<15}")
    print()
    Rank=1
    Sorted_Customers=sorted (Customers.items(),
                     key=lambda x:x[1]["Total_Revenue"],
                     reverse=True)
    
    
    for Customer,details in Sorted_Customers:
        print(f"{Rank:<15}{Customer:<15}{details["Total_Revenue"]:<15}")
        Rank+=1

def highest_revenue_day(transactions):
    Highest_Revenue={}
    for transaction in transactions:
        date, Customer_id, Product_name, Quantity, Product_Price = transaction;
        Highest_Revenue[Product_name]={
            "Date":"",
            "Total_Revenue":0
        }
    Highest_Revenue[Product_name]["Total_Revenue"]=Quantity*Product_Price
def highest_revenue_day(transactions):
    Highest_Revenue={}
    for transaction in transactions:
        date, Customer_id, Product_name, Quantity, Product_Price = transaction;
        Highest_Revenue[date]={
            "Total_Revenue":0
        }
        Highest_Revenue[date]["Total_Revenue"]+=Quantity*Product_Price
    high=sorted(Highest_Revenue.items(),
                key=lambda x:x[1]["Total_Revenue"],
                reverse=True)
    max_revenue=0
    for Date,Revenue in high:
        if Revenue["Total_Revenue"]>max_revenue:
            max_revenue=Revenue["Total_Revenue"]
            Revenue_Date=Date
    print("========== HIGHEST-REVENUE DAY ==========")
    print()
    print("Date :",Revenue_Date)
    print("Revenue :",max_revenue)
def add_new_data(transactions, new_transaction):
    transactions.append(new_transaction)
    return transactions


print("Enter 1 for Product Sales Analysis, 2 for adding new transaction:")
choice = input()
if choice == "2":
    new_transaction = input("Date (YYYY-MM-DD): "), input("Product ID: "), input("Product Name: "), int(input("Quantity: ")), int(input("Product Price: "))
    transactions = add_new_data(transactions, new_transaction)
print("========== SALES SUMMARY ==========")
Total_Quantity=0
Total_Revenue=0
Products=[]
Customers=[]
for date, Customer_id, Product_name, Quantity, Product_Price in transactions:
    Total_Quantity+=Quantity
    Total_Revenue+=Quantity*Product_Price
    if Product_name not in Products:
        Products.append(Product_name)
    if Customer_id not in Customers:
        Customers.append(Customer_id)
Total_Transactions=len(transactions)
print()
print("Total Transactions :",Total_Transactions)
print("Total Quantity Sold :",Total_Quantity)
print("Total Revenue :",Total_Revenue)
print("Unique Products :",Products)
print("Unique Customers :",Customers)
print()
Transactions=Product_Sales_Analysis(transactions)
print()
Top_Selling_Product(Transactions)
print()
Highest_Revenue_Product(Transactions)
print()
Customer_Sales_Analysis(transactions)
print()
highest_revenue_day(transactions)
