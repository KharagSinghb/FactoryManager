print("Welcome To Programming Principles Factory Manager Program :)")
# The introduction
# The productcode
productcode = int(input("Enter the product code: "))
if productcode < 100 :
    print("input less than 100. Input invalid")
    Exit()
elif productcode > 1000:
    print("input more than 1000. Input invalid")
    Exit()
else:
    print("product code accepted")
# The product name
productname = input("Enter the name of the product :")