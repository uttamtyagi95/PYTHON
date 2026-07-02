# # check even or odd
# num=int(input("Enter a no:"))
# if num % 2==0:
#     print("num is even")
# else:
#     print("num is odd")

# # larger of two no
# num1=int(input("enter first no."))
# num2=int(input("enter second no."))
# if num1>=num2:
#     print("num1 is largest")
# else:
#     print("num2 is largest")

# # check no is positive negative or zero
# num=int(input("Enter a no."))
# if num>0:
#     print("No is positive")
# elif num<0:
#     print("No is negative")
# else:
#     print("No is zero")

# # check no is divisible by 5
# num=int(input("Enter a no."))
# if num%5==0:
#     print("no is divisible")
# else:
#     print("no is non divisible")

# # find the remainder
# dividend=int(input("enter a dividend:"))
# divisor=int(input("enter a divisor:"))
# remainder=dividend%divisor
# print(remainder)

# # find the largest of three no
# num1=int(input("enter a no:"))
# num2=int(input("enter a no:"))
# num3=int(input("enter a no:"))
# if num1>=num2 & num1>=num3:
#     print("num1 is largest")
# elif num2>=num3 & num2>=num1:
#     print("num2 is largest")
# else:
#     print("num3 is largest")

# # check year is leap or not
# year=int(input("enter a year:"))
# if year%4==0:
#     print("year is leap")
# else:
#     print("year is non leap")

# # calculate the percentage of five subjects and print the grade
# subject1=float(input("Enter marks for subject1:"))
# subject2=float(input("Enter marks for subject2:"))
# subject3=float(input("Enter marks for subject3:"))
# subject4=float(input("Enter marks for subject4:"))
# subject5=float(input("Enter marks for subject5:"))
# total_marks=subject1+subject2+subject3+subject4+subject5
# percentage=(total_marks/500)*100

# if percentage>=90:
#     print ("Grade is A")
# elif percentage>=80:
#     print ("Grade is B")
# elif percentage>=70:
#     print("Grade is C")
# elif percentage>=60:
#     print("Grade is D")
# elif percentage>=50:
#     print("Grade is E")
# else:
#     print("Grade is F")
# print(f"total_marks:{total_marks}")
# print(f"percentage:{percentage}")

# # check character is vowel or consonant
# char=input("Enter a character:")
# if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u') or (char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
#   print(f"'{char} is vowel")
# elif char.isalpha() and len(char)==1:
#   print(f"'{char} is consonant")
# else:
#   print("Invalid input")

# # elibility for voting
# age=int(input("Enter a age:"))
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible for vote")    

# # create a simple calculator
# num1=float(input("Enter first number:"))
# operator=input("Enter operator(+,-,*,/):")
# num2=float(input("Enter second number:"))
# if operator=='+':
#     result=num1+num2
#     print(f"Result:{num1}+{num2}={result}")
# elif operator=='-':
#     result=num1-num2
#     print(f"Result:{num1}-{num2}={result}")
# elif operator=='*':
#     result=num1*num2
#     print(f"Result:{num1}*{num2}={result}")
# elif operator=='/':
#     result=num1-num2
#     print(f"Result:{num1}/{num2}={result}")
# else:
#     print("Invalid input")

# # check a no is multiple of both 3 and 5
# num=int(input("Enter a number"))
# if num%15==0:
#     print("Num is multiple of 3 and 5")
# else:
#     print("Num is non multiple 3 and 5")

# # find the smallest of three number
# num1=int(input("Enter first no.:"))
# num2=int(input("Enter second no.:"))
# num3=int(input("Enter third no.:"))
# if num1<=num2 & num1<=num3:
#    print("num1 is smallest")
# elif num2<num3 & num2<=num3:
#    print("num2 is smallest")
# else:
#    print("num3 is smallest")

# # create a login system with predefined username
# correct_user="admin"
# correct_pass=123
# input_user=input("Enter name:")
# input_pass=int(input("Enter pass:"))
# if input_user==correct_user and input_pass==correct_pass:
#     print("Access granted ! welcome")
# else:
#     print("Access Denied")


