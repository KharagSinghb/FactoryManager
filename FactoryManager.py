import random

class Product:
    def __init__(self, productcode, productname, costprice, sellprice, monthlyproduction, stocks):
        self.productcode = productcode
        self.productname = productname
        self.costprice = costprice
        self.sellprice = sellprice
        self.monthlyproduction = monthlyproduction
        self.stocks = stocks
        self.monthly_stock = []

    def simulate_monthly_activity(self):
        units_sold = random.randint(max(0, self.monthlyproduction - 10), 
                                     self.monthlyproduction + 10)    
        self.stocks += self.monthlyproduction - units_sold
        self.monthly_stock.append((units_sold, self.stocks))
        return units_sold
    
    def calculate_profit_loss(self):
        total_units_sold = sum(units_sold for units_sold, _ in self.monthly_stock)
        total_units_manufactured = self.monthlyproduction * len(self.monthly_stock)
        profit = (total_units_sold * self.sellprice) - (total_units_manufactured * self.costprice)
        return profit

    def display_stock_statement(self):
        print(f"\nProduct Code: {self.productcode}")
        print(f"Product Name: {self.productname}")
        print(f"Sale Price: ${self.sellprice:.2f}")
        print(f"Manufacture Cost: ${self.costprice:.2f}")
        print(f"Final Stock Level: {self.stocks}")
        print("\nPredicted Monthly Stock for the next 12 months:")
        print("Month | Units Sold | Stock Level")
        for month in range(len(self.monthly_stock)):
            units_sold, stock_level = self.monthly_stock[month]
            print(f"{month + 1:5} | {units_sold:10} | {stock_level:11}")
        profit = self.calculate_profit_loss()
        print(f"\nTotal Profit/Loss: ${profit:.2f}")

def main():
    print("Welcome To Programming Principles Factory Manager Program :)")
    
    while True:
        try:
            productcode = int(input("Enter the product code (between 100 and 1000): "))
            if 100 <= productcode <= 1000:
                break
            print("Product code must be between 100 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    productname = input("Enter the name of the product: ")

    while True:
        try:
            costprice = float(input("Enter the manufacturing cost of the product: "))
            if costprice >= 0:
                break
            print("Invalid manufacturing cost. Must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            sellprice = float(input("Enter the selling price of the product: "))
            if sellprice >= 0:
                break
            print("Invalid selling price. Must be a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            monthlyproduction = int(input("What is the number of products manufactured in a month? "))
            if monthlyproduction >= 0:
                break
            print("Invalid monthly production. Must be a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            stocks = int(input("Enter the stock level of this product: "))
            if stocks >= 0:
                break
            print("Invalid stock level. Must be a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Create the instance of Product
    product = Product(productcode, productname, costprice, sellprice, monthlyproduction, stocks)  

    # Simulate monthly production and sales for 12 months
    for _ in range(12):
        product.simulate_monthly_activity()

    # Display stock statement
    product.display_stock_statement()

if __name__ == "__main__":
    main()