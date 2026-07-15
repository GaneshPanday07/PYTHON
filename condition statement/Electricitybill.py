unit = int(input("Enter the unit of your electricity Bill: "))
rent = 100

if unit < 100:
    bill = rent
    print("your bill is =",bill)
elif unit < 200 and unit > 100:
    bill = rent+100
    print("your bill is =",bill)
elif unit < 300 and unit > 200:
    bill = rent+200
    print("your bill is =",bill)
else:
    bill = rent+300
    print("your bill is =",bill)