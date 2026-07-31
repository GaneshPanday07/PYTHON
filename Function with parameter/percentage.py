def marks(total_marks, obtained_marks):
    if total_marks == 0:
        print("total marks can't be zero")
    percentage = (obtained_marks/total_marks)*100
    if percentage >=90:
        grade = "Grade 'A'"
    elif percentage >= 80:
        grade = "Grade 'B'"
    elif percentage >=70:
        grade = "Grade 'C'"
    elif percentage >= 60:
        grade = "Grade 'D'"
    elif percentage >= 0:
        grade = "Grade 'E'"
    print(percentage,"%")
    print(grade)

marks(1000,800)
