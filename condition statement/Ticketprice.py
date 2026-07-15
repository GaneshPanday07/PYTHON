age = int(input("Enter your age: "))

if age < 18:
    print("your are child")
    print("your ticket price is =",200)
elif age > 18 and age < 60:
    print("your are adult")
    print("your ticket price is =",400)
else:
    print("your are old person")
    print("your ticket price is =", 300)