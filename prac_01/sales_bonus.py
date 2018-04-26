"""
Program to calculate and display a user's bonus on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter Sales: $"))
while sales >= 0:
    if sales < 1000:
        print("Your sales are under $1000, you will receive a 10% bonus of ${:.2f}".format(sales * .1))
    elif sales >= 1000:
        print("Your sales are equal to $1000 or more, you will receive a 15% bonus of ${:.2f}".format(sales * .15))
    sales = float(input("Enter Sales: $"))
