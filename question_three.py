# no3 i)
def user_age(age):
    age = int(input('Enter your age:'))
    if age>=18 :
        print('You are eligible')
    else:
        print('You are not eligible')
user_age(18)

# ii)
def grade_student(student_mark):
# Handling invalid input
    if student_mark == int(student_mark):
        pass
    else:
            print('invalid input')
    if student_mark>=90 and student_mark<=100 and student_mark:
        print(f"A- Excellent ")
    elif student_mark>=80 and student_mark<=89:
        print(f"B- Excellent")
    elif student_mark>=70 and student_mark<=79:
        print(f"C- Good ")
    elif student_mark>=60 and student_mark<=69:
        print(f"D- Satisfactory ")
    else:
        print(f"F- Needs improvement ")
    
    
grade_student(85)
grade_student(78)

    



