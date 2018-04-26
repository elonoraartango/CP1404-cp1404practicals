
item_count = 0
total_items = item_count + 1

total_items = int(input("Number of items"))
for i in range(total_items):
    item_price = float(input("Price of item {}:".format(i+1)))
if item_price >= 100:
    print("Total price for", total_items, "items is ${:.2f}".format(item_price-item_price * .1))
else:
    print("Total price for", total_items, "items is ${:.2f}".format(item_price))



