def calculate_change(paid,price):
    change = paid - price
    return change
snack_price = 25
print("===Snack Vending Machine===")
print(f"The price of the snack is {snack_price} Rs.")
print("Accepted coins; 1,5,10,20")

total_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Enter your 1,5,10, or 20 Rs. Coin."))
    if coin != 1 and coin != 5 and coin != 10 and coin != 20:
        print("Invalid coin. Try again.\n")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}, Total money so far: {total_inserted}")

    if total_inserted >= snack_price:
        print("Enough money inserted!")
        break
change_due = calculate_change(total_inserted,snack_price)
if change_due == 0:
    pass
else:
    print(f"Here is your snack, change is : {change_due} Rs.")

print("PURCHASE SUMMARY\n")
print("Snack Price:",snack_price)
print("Coin Inserted:",coins_inserted)
print("Total Inserted",total_inserted)
print("Change Given:",change_due)
print("=========================")
print("Thank you for your purchase!")