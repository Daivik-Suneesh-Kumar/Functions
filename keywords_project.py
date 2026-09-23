ticket_price = 30
def calculate_change(paid,ticket_price):
    change = paid - ticket_price
    return change
print("===PARKING TICKET HELPER===")
print("Accepted coin values: 1,5,10 and 25.")
total_inserted = 0
coin_inserted = 0

while True:
    coin_inserted = int(input("Please enter your coin."))
    if coin_inserted != 1 and coin_inserted != 5 and coin_inserted != 10 and coin_inserted != 25:
        print("Error. Invalid Coin.")
        continue
    else:
        total_inserted = coin_inserted
        coin_inserted = coin_inserted + 1

        if total_inserted >= ticket_price:
            print("Limit of coin reached.")
            break
        change = calculate_change(total_inserted,ticket_price)
        if change == 0:
            pass
        else:
            print(calculate_change)
print("Ticket Price:",ticket_price)
print("Coin Inserted:",coin_inserted)
print("Total Paid:",total_inserted)
print("Change Due:",calculate_change)

