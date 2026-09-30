# Canteen / Food Ordering System

menu = {
    1: ("Samosa", 15),
    2: ("Vada Pav", 25),
    3: ("Sandwich", 50),
    4: ("Pizza", 100),
    5: ("Burger", 80),
    6: ("French Fries", 60),
    7: ("Cold Drink", 40),
    8: ("Tea", 15)
}

order = []

print("=" * 45)
print("       WELCOME TO ARYA'S CANTEEN")
print("=" * 45)

while True:

    print("\n----------- MENU -----------")

    for number, (item, price) in menu.items():
        print(f"{number}. {item:<20} ₹{price}")

    print("0. Finish Order")

    choice = int(input("\nEnter item number: "))

    if choice == 0:
        break

    if choice not in menu:
        print("Invalid choice! Please select a valid item.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    item_name, price = menu[choice]
    item_total = price * quantity

    order.append((item_name, price, quantity, item_total))

    print(f"{quantity} x {item_name} added to your order.")
    print(f"Item total: ₹{item_total}")


# Calculate subtotal
subtotal = sum(item[3] for item in order)


# Apply discount
if subtotal >= 600:
    discount_rate = 15
elif subtotal >= 400:
    discount_rate = 10
elif subtotal >= 200:
    discount_rate = 5
else:
    discount_rate = 0


discount = subtotal * discount_rate / 100
final_amount = subtotal - discount


# Order Summary
print("\n")
print("=" * 55)
print("                 ORDER SUMMARY")
print("=" * 55)

if len(order) == 0:
    print("No items were ordered.")

else:
    print(f"{'Item':<20}{'Qty':<8}{'Price':<10}{'Total'}")
    print("-" * 55)

    for item_name, price, quantity, item_total in order:
        print(f"{item_name:<20}{quantity:<8}₹{price:<9}₹{item_total}")

    print("-" * 55)
    print(f"Subtotal:                         ₹{subtotal:.2f}")
    print(f"Discount ({discount_rate}%):                  -₹{discount:.2f}")
    print(f"Final Amount:                     ₹{final_amount:.2f}")

print("=" * 55)
print("       THANK YOU! VISIT AGAIN")
print("=" * 55)