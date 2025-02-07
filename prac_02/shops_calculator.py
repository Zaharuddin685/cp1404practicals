
total_price_of_items = 0
num_of_items = int(input("Number of items: "))
while num_of_items < 0:
    print("Invalid number of items")
    num_of_items = int(input("Number of items: "))

for i in range(num_of_items):
    price_of_item = float(input("Price of item: "))
    total_price_of_items += price_of_item

DISCOUNT_RATE = 0.1

if total_price_of_items > 100:
    total_price_of_items = total_price_of_items - (total_price_of_items * DISCOUNT_RATE)

print(f"Total price for {num_of_items} items is ${total_price_of_items:.2f}. ")


