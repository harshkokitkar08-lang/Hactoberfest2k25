# Your code here
def calculate_bill(units):
    bill = 0
    
    if units <= 100:
        bill = units * 4
    elif units <= 200:
        bill = 100 * 4 + (units - 100) * 5
    elif units <= 300:
        bill = 100 * 4 + 100 * 5 + (units - 200) * 6
    elif units <= 400:
        bill = 100 * 4 + 100 * 5 + 100 * 6 + (units - 300) * 7
    else:
        bill = 100 * 4 + 100 * 5 + 100 * 6 + 100 * 7 + (units - 400) * 8
    
    # Apply 10% surcharge
    bill = bill + (0.1 * bill)
    
    # Round to 1 decimal place
    return round(bill, 1)


# Driver code
if __name__ == "__main__":
    units = int(input().strip())
    print(calculate_bill(units))
