marks = int(input("Enter the marks: "))

if marks < 100 and marks > 90:
    print("Grade 'A' ")
elif marks < 91 and marks > 80:
    print("Grade 'B' ")
elif marks < 81 and marks > 70:
    print("Grade 'C' ")
elif marks < 71 and marks >= 60:
    print("Grade 'D' ")
elif marks < 60 and marks > 0:
    print("fail")
else :
    print("undefine marks")

    