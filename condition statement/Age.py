age = int(input("Enter age: "))

if age < 1 :
    print("Invalid age entered.")
elif age < 13:
    print("Child")
elif age < 19:
    print("Teenager")
elif age < 60:
    print("Adult")
else :
    print("Senior Citizen")