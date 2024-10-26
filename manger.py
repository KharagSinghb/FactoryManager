import random

class Product:
    def __init__(self, code, name, sale_price, manufacture_cost, stock_level, estimated_monthly_units):
        self.code = code
        self.name = name
        self.sale_price = sale_price
        self.manufacture_cost = manufacture_cost
        self.stock_level = stock_level
        self.estimated_monthly_units = estimated_monthly_units
        self.monthly_stock = []

    def simulate_monthly_activity(self):
        # Simulate units sold within the range
        units_sold = random.randint(max(0, self.estimated_monthly_units - 10), 
                                     self.estimated_monthly_units + 10)
        
        # Update stock level
        if self.stock_level + self.estimated_monthly_units >= 0:
            self.stock_level += self.estimated_monthly_units - units_sold
            # Store the month's units sold and current stock level
            self.monthly_stock.append((units_sold, self.stock_level))
        else:
            self.monthly_stock.append((units_sold, self.stock_level))  # Append current stock level even if negative

        return units_sold

    def calculate_profit_loss(self):
        total_units_sold = sum(units_sold for units_sold, _ in self.monthly_stock)
        total_units_manufactured = self.estimated_monthly_units * len(self.monthly_stock)
        profit = (total_units_sold * self.sale_price) - (total_units_manufactured * self.manufacture_cost)
        return profit

    def display_stock_statement(self):
        print(f"\nProduct Code: {self.code}")
        print(f"Product Name: {self.name}")
        print(f"Sale Price: ${self.sale_price:.2f}")
        print(f"Manufacture Cost: ${self.manufacture_cost:.2f}")
        print(f"Initial Stock Level: {self.stock_level}")
        print("\nPredicted Monthly Stock for the next 12 months:")
        print("Month | Units Sold | Stock Level")
        for month in range(12):
            units_sold, stock_level = self.monthly_stock[month]
            print(f"{month + 1:5} | {units_sold:10} | {stock_level:11}")
        profit = self.calculate_profit_loss()
        print(f"\nTotal Profit/Loss: ${profit:.2f}")


def main():
    print("Enter Product Details:")
    code = int(input("Product Code (100-1000): "))
    name = input("Product Name: ")
    sale_price = float(input("Product Sale Price (> 0): "))
    manufacture_cost = float(input("Product Manufacture Cost (> 0): "))
    stock_level = int(input("Initial Stock Level (> 0): "))
    estimated_monthly_units = int(input("Estimated Monthly Units Manufactured (>= 0): "))

    # Create Product instance
    product = Product(code, name, sale_price, manufacture_cost, stock_level, estimated_monthly_units)

    # Simulate monthly production and sales for 12 months
    for _ in range(12):
        product.simulate_monthly_activity()

    # Display stock statement
    product.display_stock_statement()


if __name__ == "__main__":
    main()