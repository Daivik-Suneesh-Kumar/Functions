def greet():
    print("Welcome to the store!")
greet()

price = float(input("Enter price per cup."))
cups = int(input("Enter the cups sold."))

def total_cost(price,cups):
    return price*cups
total = total_cost(price,cups)
print("Total:",round(total,2))

paid = int(input("Enter the paid amount."))

def change(total,paid):
    return total-paid
change_cost = change(total,paid)
print("Change:",round(total,2))

def thanks(cups):
    if cups >= 5:
        print("Thank u for such a big contribution!")
    else:
        print("Thank u for visiting!")
thanks(cups)    
