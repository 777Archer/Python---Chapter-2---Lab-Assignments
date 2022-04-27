"""
David Archer
CS/IS 151 Python
3-06-2022
"""

SALES_TAX = .07

print("You'll be purchasing 5 items.")
first_item_purchased = float(input ("Please enter the price of item 1: ")) 
second_item_purchased = float(input ("Please enter the price of item 2: "))
third_item_purchased = float(input ("Please enter the price of item 3: "))
fourth_item_purchased = float(input ("Please enter the price of item 4: "))
fifth_item_purchased = float(input ("Please enter the price of item 5: ") + '\n')

subtotal = float(first_item_purchased + second_item_purchased + third_item_purchased + fourth_item_purchased + fifth_item_purchased)
total_sales_tax = subtotal * SALES_TAX 
total = subtotal + total_sales_tax

print("Subtotal:\t$", format(subtotal, "9,.2f"))
print("Tax (7.00%):\t$", format(total_sales_tax, "9,.2f"))
print("Total:\t\t$", format(total, "9,.2f"))
