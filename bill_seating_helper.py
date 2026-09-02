def total_bill(bill_amnt,tip_perc):
    total = bill_amnt*(1+0.01*tip_perc)
    total = round(total,2)
    print(f"Please pay Rs.{total}")
    return total
total_bill(150,20)
def seating_arrangements(guests):
    '''Calculates number of seating arrangements for guests.'''
    if guests == 0 or guests == 1:
        return 1
    while guests > 1:
        return guests*seating_arrangements(guests-1)
    print(seating_arrangements.__doc__)
print("Seating arrangements for 1 guest:", seating_arrangements(1))
print("Seating arrangements for 2 guests:", seating_arrangements(2))
print("Seating arrangements for 3 guests:", seating_arrangements(3))
print("Seating arrangements for 5 guests:", seating_arrangements(5))

    
        
