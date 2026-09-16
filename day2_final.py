print("Welcome to the Tip Calculator!")
bill = int(input("What was your total bill?: $"))
tip = int(input("How much tip would you like to give: 10, 12, or 15?: "))
split = int(input("How many people to split the bill?: "))

if tip == 10:
    bill = (bill * 1.1) / split

elif tip == 12:
    bill = (bill * 1.12) / split

elif tip == 15:
    bill = (bill * 1.15) / split

print(f"Each person should pay: ${round(bill, 3)}")
 