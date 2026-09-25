print("Please enter the student's mark")
student_mark = int(input("Enter mark: "))
while student_mark < 0 or student_mark > 50:
    print("The student's mark should be in the range 0 to 50. Please re-enter the mark.")
    student_mark = int(input("Enter mark: "))
60
print("Valid mark:", student_mark)
