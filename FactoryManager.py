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
# The stock level
    stocks = int(input("Enter the stock level of this product"))
    if stocks < 0:
        print("Invalid stock level. Input a number greater or equal to zero")

    # create the instance product
    product = Product(productcode, productname, costprice,sellprice,stocks)  
