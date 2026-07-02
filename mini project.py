# Creating a student information program

name=input("Enter your name:")
age=int(input("Enter your age:"))
subject1=float(input("Enter your first subject marks:"))
subject2=float(input("Enter your second subject marks:"))
subject3=float(input("Enter your third subject marks:"))
total_marks=subject1+subject2+subject3
average_marks=total_marks/3
print("welcome:",name)
print("your age is:",age)
print("your total_marks is:",total_marks)
print("your average_marks is:",average_marks)

