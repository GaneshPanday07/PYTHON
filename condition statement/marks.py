m = int(input("enter the marks for know your grade: "))

if m > 90 and m < 100:
    print("Grade A")
elif m > 74 and m < 100:
    print("Grade B")
elif m > 59 and m < 100:
    print("Grade C")
elif m > 39 and m < 100:
    print("Grade D")
elif m <= 0 and m > 0:
    print("Fail")
else:
    print("invalid")


