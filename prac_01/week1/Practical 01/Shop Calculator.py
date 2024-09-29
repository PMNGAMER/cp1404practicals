DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1
total_price = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))

for i in range(items):
    item_price = float(input("Price of item: "))
    total_price += item_price
    
if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price - (total_price * DISCOUNT_RATE)
print(f"Total price for {items} items is ${total_price:.2f}")