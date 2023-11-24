# sample code code for basic retail forecast calculation
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_company = input("Enter your employer: ")
sales_ly = input("Enter last year's sales units: ")
sellthru_ly = input("Enter last year's dollar sellthru: ")

# user info to setup environment
if user_name == "JC":
    print("Welcome to Rightward!")
else:
    print("Welcome to", user_company)

# calculation formulas
sales_ly += 200
sales_fcst_sellthru = .85
sales_fcst_sellthru_pretty = sales_fcst_sellthru * 100
sales_fcst = sales_ly / sales_fcst_sellthru

# print actual results for customers
print(user_age + 10)
print("Your sales LY were", sales_ly)
print("Your sellthru LY was {:.2f}%".format(sellthru_ly))
print("Your forecast ship dollars are", sales_fcst)
print("Your forecast sellthru is {:.2f}%".format(sales_fcst_sellthru_pretty))
