import random

class Product:
    def _init_(self,productcode,productname,costprice,sellprice,monthlyproduction,stocks):
        self.productcode = productcode
        self.productname = productname
        self.costprice = costprice
        self.sellprice = sellprice
        self.monthlyproduction = monthlyproduction
        self.stocks = stocks
        self.monthly_stock = []

    def simulate_monthly_activity(self):
        # Simulate units sold within the range
        units_sold = random.randint(max(0, self.monthlyproduction - 10), 
                                     self.monthlyproduction + 10)    

        # Update stock level
        if self.stocks + self.monthlyproduction >= 0:
            self.stocks += self.monthlyproduction - units_sold
            # Store the month's units sold and current stock level
            self.monthly_stock.append((units_sold, self.stocks))
        else:
            self.monthly_stock.append((units_sold, self.stocks))  # Append current stock level even if negative

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
        print(f"Initial Stock Level: {self.stocks}")
        print("\nPredicted Monthly Stock for the next 12 months:")
        print("Month | Units Sold | Stock Level")
        for month in range(12):
            units_sold, stock_level = self.monthly_stock[month]
            print(f"{month + 1:5} | {units_sold:10} | {stock_level:11}")
        profit = self.calculate_profit_loss()
        print(f"\nTotal Profit/Loss: ${profit:.2f}")



def main():
    print("Welcome To Programming Principles Factory Manager Program :)")
# The introduction
# The productccode
    productcode = int(input("Enter the product code: "))
    if productcode < 100 :
        print("input less than 100. Input invalid")
        exit()
    elif productcode > 1000:
        print("input more than 1000. Input invalid")
        exit()
    else:
        print("product code accepted")
# The product name
    productname = input("Enter the name of the product :")
# The manufacture cost
    costprice = float(input("Enter the manufacturing cost of the product"))
    if costprice < 0:
        print("Invalid manufacturing cost of the product")
        exit()
    else :
        print("The manufacturing cost of the product is ",costprice)

# the selling price
    sellprice = float(input("enter the selling price of the product"))
    if sellprice < 0:
        print("Entered selling price invalid")
        exit()        

# manufacturing estimate 
    monthlyproduction = int(input("what are the number of products manufactured in a month: "))       
    if monthlyproduction < 0:
        print("Invalid monthly production")
        exit() 
# The stock level
    stocks = int(input("Enter the stock level of this product"))
    if stocks < 0:
        print("Invalid stock level. Input a number greater or equal to zero")

    # create the instance product
    product = Product(productcode, productname, costprice,sellprice, monthlyproduction,stocks)  

    # Simulate monthly production and sales for 12 months
    for _ in range(12):
        product.simulate_monthly_activity()

    # Display stock statement
    product.display_stock_statement()


if __name__ == "__main__":
    main()