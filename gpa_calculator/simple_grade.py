# Simple Grade Calculator
mark = int(input("Enter your mark: "))

if (mark >= 90 and mark <= 100):
    grade = 'O'
    grade_point = 10.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Pass")
elif (mark >= 80 and mark < 90):
    grade = 'A+'
    grade_point = 9.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Pass")
elif (mark >= 70 and mark < 80):
    grade = 'A'
    grade_point = 8.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Pass")
elif (mark >= 60 and mark < 70):
    grade = 'B+'
    grade_point = 7.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Pass")
elif (mark >= 50 and mark < 60):
    grade = 'B'
    grade_point = 6.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Pass")
elif (mark >= 45 and mark < 50):
    grade = 'C'
    grade_point = 5.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Pass")
else:
    grade = 'U'
    grade_point = 0.0
    print("Grade = ", grade)
    print("Grade Point = ", grade_point)
    print("Result = Fail") 